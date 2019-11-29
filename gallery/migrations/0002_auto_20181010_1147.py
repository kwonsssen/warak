# Generated by Django 2.1.2 on 2018-10-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': '갤러리', 'verbose_name_plural': '갤러리'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='classify',
            field=models.CharField(choices=[('inside', '센터 내 프로그램'), ('school', '학교 진행 프로그램'), ('outside', '외부 프로그램'), ('others', '기타')], max_length=10, verbose_name='분류'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='사진명'),
        ),
    ]
