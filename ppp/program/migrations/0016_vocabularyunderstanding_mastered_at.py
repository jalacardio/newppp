# Generated by Django 3.0 on 2020-10-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0015_auto_20201025_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabularyunderstanding',
            name='mastered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
