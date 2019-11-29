from django.db import models
from django.utils.translation import ugettext_lazy as _
class HomePhoto(models.Model):
    class Meta:
        verbose_name = _("메인사진첩")
        verbose_name_plural = _("메인사진첩")
    title = models.CharField('위치', max_length=50)
    photo = models.ImageField(
        verbose_name='메인 사진',
        upload_to="mainPhoto/",
        )

class Employee(models.Model):
    class Meta:
        verbose_name = _("직원")
        verbose_name_plural = _("직원")
    name    = models.CharField('이름',max_length=20)
    position = models.CharField('직위', max_length=20)
    career =  models.TextField('업무', blank=True,null=True)
    photo = models.ImageField(
        verbose_name='사진',
        upload_to="Employee/",
        )

class PopUp(models.Model):
    class Meta:
        verbose_name =_('팝업창 수정')
        verbose_name_plural = _("팝업창 수정")
    title = models.CharField('제목',blank=True,max_length=255)
    is_view = models.BooleanField('활성화 여부',default=True)
    image =  image = models.ImageField(
                    verbose_name='사진',
                    upload_to="popup/%Y/%m/%d",
                    blank=False,
                    null=False
                )
    created_at = models.DateTimeField(auto_now_add=True)