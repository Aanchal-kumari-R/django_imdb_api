# Generated by Django 5.0.7 on 2024-09-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_api', '0005_alter_review_review_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
