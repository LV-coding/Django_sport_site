# Generated by Django 4.0.4 on 2022-05-20 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabata', '0003_rename_create_date_article_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.CreateModel(
            name='UserTraining',
            fields=[
                ('user_training_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('comment', models.TextField()),
                ('exercise1', models.CharField(max_length=64)),
                ('exercise2', models.CharField(max_length=64)),
                ('exercise3', models.CharField(max_length=64)),
                ('exercise4', models.CharField(max_length=64)),
                ('exercise5', models.CharField(max_length=64)),
                ('exercise6', models.CharField(max_length=64)),
                ('exercise7', models.CharField(max_length=64)),
                ('exercise8', models.CharField(max_length=64)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
