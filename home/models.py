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

class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    # body = StreamField(
    #     BaseStreamBlock(), verbose_name="Page body", blank=True
    # )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        # FieldPanel('body'),
    ]