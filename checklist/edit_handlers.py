# checklist/edit_handlers.py
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.admin.panels import Panel

class ChecklistPanel(Panel):
    """
    A small, Wagtail-compatible custom Panel.
    It MUST define template_name at the class level so the BoundPanel exposes it.
    """
    class BoundPanel(Panel.BoundPanel):
        template_name = "checklist/panel.html"