from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Notice(models.Model):
    class Meta:
        verbose_name = _("공지사항")
        verbose_name_plural = _("공지사항")
    title = models.CharField('제목',max_length=256)
    content = models.TextField('내용')
    image = models.ImageField(
                    verbose_name='사진',
                    upload_to="notice/%Y/%m/%d",
                    blank=True,
                    null=True
                )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title