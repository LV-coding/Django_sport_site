from django.urls import path
from . import views
from .sitemaps import StaticSitemap, ArticleSitemap, TrainingSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static':StaticSitemap,
    'article':ArticleSitemap,
    'training': TrainingSitemap
}

urlpatterns = [
    path('', views.about_tabata, name='index'),
    path('about', views.about_site, name='about'),
    path('training/', views.get_trainings, name='training'),
    path('training/<int:training_id>', views.view_training, name='view_training'),
    path('training/<int:training_id>/change', views.change_training_published, name='change_training_published'),
    path('error/', views.error_content, name='error_content'),
    path('article/', views.get_articles, name="article"),
    path('article/<int:article_id>', views.view_article, name='view_article'),
    path('article/<int:article_id>/change', views.change_article_published, name='change_article_published'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('personal_consent', views.personal_consent, name='personal_consent'),
    path('account', views.account_view, name='account'),
    path('account/<int:user_training_id>', views.view_account_training, name='view_account_training'),
    path('account/create', views.create_user_training, name='create_user_training'),
    path('account/<int:user_training_id>/delete', views.delete_user_training, name='delete_user_training'),
    path('account/<int:user_training_id>/edit', views.edit_user_training, name='edit_user_training'),
    path('account/changepassword', views.change_password, name='changepassword'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", views.robots_txt),
]





