from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from .models import ChecklistItem

class ChecklistItemViewSet(SnippetViewSet):
    model = ChecklistItem
    menu_label = 'Checklist Items'
    icon = 'list-ul'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'page', 'is_done')
    search_fields = ('title',)

register_snippet(ChecklistItemViewSet)

@hooks.register('before_publish_page')
def check_checklist_completion(request, page):
    """
    Blocks publishing if any checklist item for this page is not marked as done.
    """
    # Check if the page has checklist items
    if hasattr(page, 'checklist_items') and page.checklist_items.exists():
        incomplete_items = page.checklist_items.filter(is_done=False)
        
        if incomplete_items.exists():
            # Add an error message to the page
            msg = _("You cannot publish this page because the following checklist items are incomplete: %(items)s") % {
                'items': ", ".join([item.title for item in incomplete_items])
            }
            page.add_error(None, msg)
            # Raise ValidationError to stop the publish action
            raise ValidationError(msg)

@hooks.register("insert_editor_js")
def checklist_js():
    # simple, safe JS string — console message dikhayega
    return """
    <script>
    // Debug message for Wagtail page editor
    console.log("Checklist panel loaded successfully!");
    </script>
    """