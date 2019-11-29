# Generated by Django 2.1.2 on 2018-10-09 14:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='제목')),
                ('classify', models.CharField(max_length=256, verbose_name='분류')),
                ('target', models.CharField(max_length=256, verbose_name='대상')),
                ('start_schedule', models.DateTimeField(verbose_name='일정 시작일')),
                ('end_schdule', models.DateTimeField(verbose_name='일정 종료일')),
                ('start_signup_day', models.DateTimeField(verbose_name='신청 시작일')),
                ('end_signup_day', models.DateTimeField(verbose_name='신청 종료일')),
                ('content', models.TextField(verbose_name='내용')),
            ],
            options={
                'verbose_name': '프로그램',
                'verbose_name_plural': '프로그램 리스트',
            },
        ),
        migrations.CreateModel(
            name='ProgramSignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='학생이름')),
                ('school', models.CharField(max_length=256, verbose_name='출석학교')),
                ('school_year', models.IntegerField(verbose_name='학년')),
                ('gender', models.CharField(choices=[('M', '남자'), ('W', '여자')], max_length=2, verbose_name='성별')),
                ('contact', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(message='전화번호를 제대로 입력해주세요.', regex='^010[1-9]\\d{7}$')], verbose_name='연락처')),
                ('guardian_name', models.CharField(max_length=256, verbose_name='신청인 이름')),
                ('guardian_contact', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(message='전화번호를 제대로 입력해주세요.', regex='^010[1-9]\\d{7}$')], verbose_name='보호자 연락처')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program', verbose_name='프로그램')),
            ],
            options={
                'verbose_name': '프로그램 신청인',
                'verbose_name_plural': '프로그램신청인 리스트',
            },
        ),
    ]
