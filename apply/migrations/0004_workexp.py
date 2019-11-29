# Generated by Django 2.1.2 on 2018-10-15 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_auto_20181009_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='신청인 이름')),
                ('telephone', models.TextField(verbose_name='연락처')),
                ('address', models.TextField(verbose_name='주소')),
                ('email', models.TextField(verbose_name='이메일')),
                ('content', models.TextField(verbose_name='신청내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='신청일')),
            ],
            options={
                'verbose_name': '직업체험일터',
                'verbose_name_plural': '직업체험일터',
            },
        ),
    ]