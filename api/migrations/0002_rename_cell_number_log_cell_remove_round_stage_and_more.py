# Generated by Django 4.0.5 on 2022-06-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='cell_number',
            new_name='cell',
        ),
        migrations.RemoveField(
            model_name='round',
            name='stage',
        ),
        migrations.AddField(
            model_name='round',
            name='current_attempt',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='current attempt number'),
            preserve_default=False,
        ),
    ]