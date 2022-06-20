from django.contrib import admin
from .models import User, Training, Article, UserTraining, PersonalConsert


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'complexity', 'equipment')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_date')

class UserTrainingAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')

admin.site.register(Training, TrainingAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserTraining, UserTrainingAdmin)
admin.site.register(User)
admin.site.register(PersonalConsert)
