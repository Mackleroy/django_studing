# Generated by Django 3.1.7 on 2021-03-15 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
