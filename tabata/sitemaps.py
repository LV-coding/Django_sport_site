from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Training, Article

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['index', 'about', 'training', 'error_content', 'article', 'login', 'register', 'personal_consent']

    def location(self, item):
        return reverse(item)

class ArticleSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.9

    def items(self):
        return Article.objects.filter(published=True)

    def location(self, item):
        return f'/article/{item.article_id}'

class TrainingSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.9

    def items(self):
        return Training.objects.filter(published=True)

    def location(self, item):
        return f'/training/{item.training_id}'
