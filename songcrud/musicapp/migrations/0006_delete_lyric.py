# Generated by Django 4.1.2 on 2022-11-08 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_remove_song_id_song_song_id_alter_lyric_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lyric',
        ),
    ]