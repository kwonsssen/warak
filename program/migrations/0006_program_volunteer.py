# Generated by Django 2.0.7 on 2018-12-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_auto_20181009_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='volunteer',
            field=models.IntegerField(default=0, verbose_name='지원자'),
        ),
    ]
