# Generated by Django 4.1.1 on 2022-09-22 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0003_alter_aboutme_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='kontakts_habr',
            new_name='contakts_habr',
        ),
        migrations.RenameField(
            model_name='aboutme',
            old_name='kontakts_pikabu',
            new_name='contakts_pikabu',
        ),
        migrations.RenameField(
            model_name='aboutme',
            old_name='kontakts_tg',
            new_name='contakts_tg',
        ),
        migrations.RenameField(
            model_name='aboutme',
            old_name='kontakts_vk',
            new_name='contakts_vk',
        ),
        migrations.RenameField(
            model_name='aboutme',
            old_name='kontakts_youtube',
            new_name='contakts_youtube',
        ),
    ]
