# Generated by Django 4.0.4 on 2022-06-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabata', '0007_alter_article_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title_image',
            field=models.CharField(max_length=512),
        ),
    ]
