# Generated by Django 4.0.3 on 2022-04-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_articles_options_alter_articles_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=160),
        ),
    ]
