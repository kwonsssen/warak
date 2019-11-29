# Generated by Django 2.1.2 on 2018-10-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_programsignup_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': '프로그램', 'verbose_name_plural': '프로그램'},
        ),
        migrations.AlterModelOptions(
            name='programsignup',
            options={'verbose_name': '프로그램 신청인', 'verbose_name_plural': '프로그램신청인'},
        ),
        migrations.AddField(
            model_name='program',
            name='photo',
            field=models.ImageField(default=1, upload_to='program/%Y/%m/%d', verbose_name='프로그램 사진'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='programsignup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='신청일'),
        ),
    ]