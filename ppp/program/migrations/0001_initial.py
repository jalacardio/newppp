# Generated by Django 3.0.8 on 2020-07-28 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0003_wordanalysis'),
        ('member', '0002_auto_20200720_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_date', models.DateTimeField(blank=True, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyUnderstanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary_understandings', to='member.Member')),
                ('vocabulary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_understandings', to='dictionary.Word')),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('participant', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('enrollments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary_programs', to='program.ProgramEnrollment')),
                ('words', models.ManyToManyField(to='dictionary.Word')),
            ],
        ),
        migrations.CreateModel(
            name='SubVocabularyProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_programs', to='member.Member')),
                ('vocabulary_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_programs', to='program.VocabularyProgram')),
                ('words', models.ManyToManyField(to='dictionary.Word')),
            ],
        ),
    ]
