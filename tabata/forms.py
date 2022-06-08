from django import forms
from .models import UserTraining

class UserTrainingForm(forms.ModelForm):

    class Meta:
        model = UserTraining
        fields = ('title', 'exercise1', 'exercise2', 'exercise3', 'exercise4', 
                    'exercise5', 'exercise6', 'exercise7', 'exercise8', 'comment')

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder' : 'Назва', 'class' : 'content__form-wrapper__form__training'}),
            'exercise1': forms.TextInput(attrs={'placeholder' : 'Вправа 1', 'class' : 'content__form-wrapper__form__training'}),
            'exercise2': forms.TextInput(attrs={'placeholder' : 'Вправа 2', 'class' : 'content__form-wrapper__form__training'}),
            'exercise3': forms.TextInput(attrs={'placeholder' : 'Вправа 3', 'class' : 'content__form-wrapper__form__training'}),
            'exercise4': forms.TextInput(attrs={'placeholder' : 'Вправа 4', 'class' : 'content__form-wrapper__form__training'}),
            'exercise5': forms.TextInput(attrs={'placeholder' : 'Вправа 5', 'class' : 'content__form-wrapper__form__training'}),
            'exercise6': forms.TextInput(attrs={'placeholder' : 'Вправа 6', 'class' : 'content__form-wrapper__form__training'}),
            'exercise7': forms.TextInput(attrs={'placeholder' : 'Вправа 7', 'class' : 'content__form-wrapper__form__training'}),
            'exercise8': forms.TextInput(attrs={'placeholder' : 'Вправа 8', 'class' : 'content__form-wrapper__form__training'}),
            'comment': forms.Textarea(attrs={'placeholder' : 'Ваш коментар', 'class' : 'content__form-wrapper__form__comment'})
        }
