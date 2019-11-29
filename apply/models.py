from django.db import models
from django.utils.translation import ugettext_lazy as _

class Mento(models.Model):
    class Meta:
        verbose_name = _("멘토")
        verbose_name_plural = _("멘토신청인")
    name        = models.TextField('신청인 이름')
    telephone   = models.TextField('연락처')
    schoolinfo     = models.TextField('학교 및 학년')
    email       = models.TextField('이메일')
    content     = models.TextField('신청내용')
    info_agree  = models.BooleanField("개인정보 동의")
    created_at   = models.DateTimeField('신청일',auto_now_add=True)

def __str__(self):
    return self.name

class Volunteer(models.Model):
    class Meta:
        verbose_name = _("자원봉사")
        verbose_name_plural = _("자원봉사신청인")
    name        = models.TextField('신청인 이름')
    telephone   = models.TextField('연락처')
    schoolinfo     = models.TextField('학교 및 학년')
    email       = models.TextField('이메일')
    content     = models.TextField('신청내용')
    info_agree  = models.BooleanField("개인정보 동의")
    created_at   = models.DateTimeField('신청일',auto_now_add=True)

    def __str__(self):
        return self.name

class WorkExp(models.Model):
    class Meta:
        verbose_name = _("직업체험일터")
        verbose_name_plural = _("직업체험일터")
    name        = models.TextField('신청인 이름')
    telephone   = models.TextField('연락처')
    schoolinfo     = models.TextField('학교 및 학년')
    email       = models.TextField('이메일')
    content     = models.TextField('신청내용')
    info_agree  = models.BooleanField("개인정보 동의")
    created_at   = models.DateTimeField('신청일',auto_now_add=True)

    def __str__(self):
        return self.name