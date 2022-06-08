from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)


class Training(models.Model):
    choice_of_complexity = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard')              
    )
    training_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    complexity = models.CharField(choices=choice_of_complexity, default='easy', max_length=10)
    equipment = models.BooleanField(default=False)

    def change_published(self):
        if self.published == True:
            self.published = False
        else:
            self.published = True

    def __str__(self):
        return self.title

class UserTraining(models.Model):
    user_training_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=64) 
    comment = models.TextField()
    exercise1 = models.CharField(max_length=64)
    exercise2 = models.CharField(max_length=64)
    exercise3 = models.CharField(max_length=64)
    exercise4 = models.CharField(max_length=64)
    exercise5 = models.CharField(max_length=64)
    exercise6 = models.CharField(max_length=64)
    exercise7 = models.CharField(max_length=64)
    exercise8 = models.CharField(max_length=64)
    
    def __str__(self):
        return self.title


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    title_image = models.ImageField(blank=True) #, upload_to='images/'
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def change_published(self):
        if self.published == True:
            self.published = False
        else:
            self.published = True
    
    def __str__(self):
        return self.title
    
