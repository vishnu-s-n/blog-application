# Generated by Django 4.0.4 on 2022-08-22 13:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postapi', '0002_alter_posts_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
