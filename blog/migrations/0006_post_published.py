# Generated by Django 3.1.7 on 2021-03-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_moderation'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]
