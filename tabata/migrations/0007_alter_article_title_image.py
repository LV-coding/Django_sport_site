# Generated by Django 4.0.4 on 2022-06-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabata', '0006_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
