# checklist/edit_handlers.py
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.admin.panels import Panel

class ChecklistPanel(Panel):
    """
    A small, Wagtail-compatible custom Panel.
    It MUST define template_name at the class level so the BoundPanel exposes it.
    """
    template_name = "checklist/panel.html"   # <-- make sure this path matches your template file

    def render_html(self, bound_panel):
        """
        Return safe HTML for the bound panel.
        bound_panel.instance is the Page instance the panel is attached to.
        """
        context = {
            "panel": bound_panel,
            "instance": bound_panel.instance,
        }
        return mark_safe(render_to_string(self.template_name, context))