# Generated by Django 2.0.7 on 2018-10-26 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='career',
            field=models.TextField(blank=True, null=True, verbose_name='업무'),
        ),
    ]