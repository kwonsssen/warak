from django.db import models
from django.utils.translation import ugettext_lazy as _

class Gallery(models.Model):
    class Meta:
        verbose_name = _("갤러리")
        verbose_name_plural = _("갤러리")
    gallery_filter  = (
        ('inside','센터 내 프로그램'),
        ('school','학교 진행 프로그램'),
        ('outside','외부 프로그램'),
        ('others','기타'),
    )
    name        = models.CharField('사진명', max_length=256,blank=True,null=True)
    classify    = models.CharField('분류',max_length=10, choices=gallery_filter,)
    photo       = models.ImageField(
                    verbose_name='갤러리 사진',
                    upload_to="Gallery/%Y/%m/%d",
                )
    date        = models.DateTimeField('날짜')
    
    def __str__(self):
        if not self.name:
            return "이름없음"
        return self.name