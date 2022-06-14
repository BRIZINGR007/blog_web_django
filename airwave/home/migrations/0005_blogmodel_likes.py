# Generated by Django 3.2.5 on 2022-05-01 07:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='likes',
            field=models.ManyToManyField(related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
