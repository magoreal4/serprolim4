from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    # StreamFieldPanel,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from wmetadata.models import MetadataPageMixin

class HomePage(MetadataPageMixin, Page):
    def save(self, *args, **kwargs):
        print("Se actualizó los valores home, borrando cache")
        cache.clear()
        return super().save(*args, **kwargs)

    subpage_types = [
        # 'blog.BlogIndexPage',
        'base.StandardPage'
    ]