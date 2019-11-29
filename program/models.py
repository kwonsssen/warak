from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

class Program(models.Model):
    class Meta:
        verbose_name = _("프로그램")
        verbose_name_plural = _("프로그램")
    title               = models.CharField('제목', max_length=256)
    classify            = models.CharField('분류', max_length=256)
    target              = models.CharField('대상', max_length=256)
    start_schedule      = models.DateTimeField('일정 시작일')
    end_schedule         = models.DateTimeField('일정 종료일')
    start_signup_day    = models.DateTimeField('신청 시작일')
    end_signup_day      = models.DateTimeField('신청 종료일')
    content             = models.TextField('내용')
    photo               = models.ImageField(
                            verbose_name='프로그램 사진',
                            upload_to="program/%Y/%m/%d",
                        )
    volunteer = models.IntegerField('지원자',default=0)
    volunteer_max = models.IntegerField('최대지원자',default=0)
    def __str__(self):
        return self.title

class ProgramSignUp(models.Model):
    class Meta:
        verbose_name = _("프로그램 신청인")
        verbose_name_plural = _("프로그램신청인")
    genders = (
        ('M','남자'),
        ('W','여자'),
    )
    program             = models.ForeignKey(Program,on_delete=models.CASCADE,verbose_name='프로그램')
    name                = models.CharField('학생이름', max_length=256)
    school              = models.CharField('출석학교', max_length=256)
    school_year         = models.IntegerField('학년')
    gender              = models.CharField('성별',max_length=2, choices=genders,)
    # phone_regex         = RegexValidator(regex=r'^010[1-9]\d{7}$', message="전화번호를 제대로 입력해주세요.")
    email               = models.CharField("이메일", max_length=256 , default="warak@warak.or.kr")
    contact             = models.CharField('연락처', max_length=256,)
    guardian_name       = models.CharField('신청인 이름',max_length=256)
    guardian_contact    = models.CharField('보호자 연락처', max_length=256,)
    created_at          = models.DateTimeField('신청일',auto_now_add=True)

    def __str__(self):
        return self.guardian_name
    
