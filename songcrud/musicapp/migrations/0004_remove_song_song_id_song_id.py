# Generated by Django 4.1.2 on 2022-11-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_song_likes_alter_song_song_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_id',
        ),
        migrations.AddField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]