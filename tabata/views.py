from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Training, Article, User, UserTraining
from django.urls import reverse
from markdown2 import markdown
from functools import lru_cache
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .util import password_validator
from .forms import UserTrainingForm
from django.views.decorators.http import require_GET



def about_tabata(request):
    return render(request, 'tabata/index.html')

def about_site(request):
    return render(request, 'tabata/about.html')


@lru_cache
def get_trainings(request):
    if request.user.is_superuser:
        trainings = Training.objects.all().order_by('-training_id')
    else:
        trainings = Training.objects.filter(published=True).order_by('-training_id')

    return render(request, 'tabata/training.html', {
        'trainings': trainings
    })

def error_content(request):
    return render(request, 'tabata/error_content.html')


def view_training(request, training_id):
    try:
        training = Training.objects.get(training_id=training_id)
        if request.user.is_superuser or training.published:
            text_markdown = markdown(training.text)
            return render(request, 'tabata/view_training.html', {
            'training': training,
            'text_markdown':text_markdown
            })
        else:
            return HttpResponseRedirect(reverse('index'))
    except:                                                     # if the requested ID does not exist
        return HttpResponseRedirect(reverse('error_content'))


@lru_cache
def get_articles(request):
    if request.user.is_superuser:
        articles = Article.objects.all().order_by('-article_id')
    else:
        articles = Article.objects.filter(published=True).order_by('-article_id')
    return render(request, 'tabata/article.html', {
        'articles': articles
    })

def view_article(request, article_id):
    try:
        article = Article.objects.get(article_id=article_id)
        if request.user.is_superuser or article.published:
            text_markdown = markdown(article.text)
            return render(request, 'tabata/view_article.html', {
            'article': article,
            'text_markdown':text_markdown
            })
        else:
            return HttpResponseRedirect(reverse('index'))
    except:                                                     # if the requested ID does not exist
        return HttpResponseRedirect(reverse('error_content'))


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            msg = 'Хибний логін або пароль'
            return render(request, 'tabata/login.html', {
                'msg':msg
            })
    else:
        return render(request, 'tabata/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        agree = request.POST.get('agree', False)

        if agree:
            if password != confirm_password:
                msg = 'Паролі мають співпадати!'
                return render(request, 'tabata/register.html', {
                    'msg':msg
                })
            if password_validator(password):
                try:
                    user = User.objects.create_user(username, email, password)

                except IntegrityError:
                    msg = 'Такий користувач вже існує!'
                    return render(request, 'tabata/register.html', {
                        'msg':msg
                    })

                except ValueError:
                    msg = 'Помилка значень. Можливо, форма пуста...'
                    return render(request, "tabata/register.html", {
                        'msg':msg
                    })
                
                login(request, user)
                return HttpResponseRedirect(reverse("account"))
            else:
                msg = 'Пароль повинен бути не менше 8 символів, містити великі і малі букви та цифри'
                return render(request, "tabata/register.html", {
                    'msg':msg
                    })
        else:
            msg = 'Для реєстрація потрібна згода на обробку персональних даних'
            return render(request, "tabata/register.html", {
                    'msg':msg
                })
    else:
        return render(request, "tabata/register.html")

def personal_consent(request):
    return render(request, 'tabata/personal_consent.html')


def account_view(request):
    if request.user.is_authenticated:
        user_trainings = UserTraining.objects.filter(author=request.user).order_by('-user_training_id')
        return render(request, 'tabata/account.html', {
            'user_trainings':user_trainings
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def view_account_training(request, user_training_id):
    if request.user.is_authenticated:
        try:
            user_training = UserTraining.objects.get(author=request.user, user_training_id=user_training_id)
            return render(request, 'tabata/view_account_training.html', {
            'user_training':user_training
        })
        except:
            return HttpResponseRedirect(reverse("error_content")) # if one user wants to watch another user workout
    else:
        return HttpResponseRedirect(reverse("login"))


def create_user_training(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            form = UserTrainingForm(request.POST)
            if form.is_valid():
                user_training = form.save(commit=False)
                user_training.author = request.user
                user_training.save()
                return HttpResponseRedirect(reverse("account"))
        else:
            form = UserTrainingForm()
            return render(request, 'tabata/create_user_training.html', {
                'form':form
            })
    else:
        return HttpResponseRedirect(reverse("login"))


def delete_user_training(request, user_training_id):
    if request.user.is_authenticated:
        try:
            user_training = UserTraining.objects.get(author=request.user, user_training_id=user_training_id)
            user_training.delete()
            return HttpResponseRedirect(reverse("account"))
        except:
            return HttpResponseRedirect(reverse("error_content")) # if one user wants to watch another user workout
    else:
        return HttpResponseRedirect(reverse("login"))


def edit_user_training(request, user_training_id):
    user_training = UserTraining.objects.get(user_training_id=user_training_id)
    if request.user.is_authenticated and user_training.author == request.user: 
        if request.method == 'POST':
            form = UserTrainingForm(request.POST, instance=user_training)
            if form.is_valid():
                user_training = form.save(commit=False)
                user_training.author = request.user
                user_training.save()
                return HttpResponseRedirect(reverse("account"))
        else:
            form = UserTrainingForm(instance=user_training)
            return render(request, 'tabata/edit_user_training.html', {
                'form':form
            })
    else:
        return HttpResponseRedirect(reverse("login"))


@login_required
def change_password(request):
    if request.method == 'POST':
        user = User.objects.get(user_id=request.user.user_id)
        old_password = request.POST['old_password']
        if check_password(old_password, request.user.password):
            new_password = request.POST['new_password']
            confirm_new_password = request.POST['confirm_new_password']
            if new_password == confirm_new_password:
                if password_validator(new_password):
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    msg = 'Пароль успішно змінений'
                    return render(request, 'tabata/changepassword.html', {
                    'msg':msg
                    })
                else:
                    msg = 'Пароль повинен бути не менше 8 символів, містити великі і малі букви та цифри'
                    return render(request, 'tabata/changepassword.html', {
                    'msg':msg
                    })
            else:
                msg = 'Паролі мають співпадати'
                return render(request, 'tabata/changepassword.html', {
                'msg':msg
                })
        else:
            msg = 'Хибний старий пароль'
            return render(request, 'tabata/changepassword.html', {
                'msg': check_password(old_password, request.user.password)
            })
    else:
        return render(request, 'tabata/changepassword.html')


def change_training_published(request, training_id):
    if request.user.is_superuser:
        training = Training.objects.get(training_id=training_id)
        training.change_published()
        training.save()
        return HttpResponseRedirect(reverse('view_training', args=(training_id,)))
    else:
        return HttpResponseRedirect(reverse("index"))

def change_article_published(request, article_id):
    if request.user.is_superuser:
        article = Article.objects.get(article_id=article_id)
        article.change_published()
        article.save()
        return HttpResponseRedirect(reverse('view_article', args=(article_id,)))
    else:
        return HttpResponseRedirect(reverse("index"))

#def view_robots(request):
    #return render(request, 'tabata/robots.txt')

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /account/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")