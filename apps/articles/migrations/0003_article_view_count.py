# Generated by Django 4.1.2 on 2023-11-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
