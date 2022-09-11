from django.db import models
from django.utils.translation import gettext_lazy as _


from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    # StreamFieldPanel,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting



class HomePage(Page):
    pass
    # subpage_types = [
    #     'blog.BlogIndexPage',
    #     'base.StandardPage'
    # ]

