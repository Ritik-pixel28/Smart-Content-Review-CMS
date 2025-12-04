from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class ChecklistItem(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="checklist_items")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, help_text="Optional description for this checklist item")
    is_done = models.BooleanField(default=False)

    panels = [
        FieldPanel('page'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('is_done'),
    ]

    def __str__(self):
        return self.title
