# Generated by Django 4.1.2 on 2022-11-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='id',
        ),
        migrations.AddField(
            model_name='song',
            name='song_id',
            field=models.CharField(default=1, max_length=25, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
