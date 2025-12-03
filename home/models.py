from checklist.edit_handlers import ChecklistPanel
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.db import models


class HomePage(Page):
    body = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        ChecklistPanel(),   # <-- NEW PANEL
    ]