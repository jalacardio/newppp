# Generated by Django 3.0 on 2020-10-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0013_delete_programprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='progress',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
