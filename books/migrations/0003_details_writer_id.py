# Generated by Django 5.0.3 on 2024-04-14 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_authors_details_genre_homepage_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='writer_id',
            field=models.IntegerField(default=0),
        ),
    ]
