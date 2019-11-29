from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NoticeConfig(AppConfig):
    name = 'notice'
    verbose_name = _('공지사항')