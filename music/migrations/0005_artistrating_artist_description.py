# Generated by Django 4.0.3 on 2022-03-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_artistrating_rating_alter_songrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistrating',
            name='artist_description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]