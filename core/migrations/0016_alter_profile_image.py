# Generated by Django 4.0.3 on 2022-05-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_articles_picture_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/images/default/defaultProfile.png', upload_to='profile_pics'),
        ),
    ]