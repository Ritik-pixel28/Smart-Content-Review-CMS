from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from .models import ChecklistItem
from .dashboard import ChecklistSummaryPanel

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
            # Create error message listing incomplete items
            msg = _("You cannot publish this page because the following checklist items are incomplete: %(items)s") % {
                'items': ", ".join([item.title for item in incomplete_items])
            }
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

@hooks.register('construct_homepage_panels')
def add_checklist_dashboard_panel(request, panels):
    """
    Add checklist summary panel to the Wagtail admin homepage.
    """
    panels.append(ChecklistSummaryPanel())

@hooks.register('construct_page_listing_buttons')
def add_checklist_status_badge(buttons, page, **kwargs):
    """
    Add a status badge and icon to pages with checklist items in the dashboard.
    """
    if hasattr(page, 'checklist_items') and page.checklist_items.exists():
        incomplete_count = page.checklist_items.filter(is_done=False).count()
        total_count = page.checklist_items.count()
        
        if incomplete_count > 0:
            # Add warning badge with icon for incomplete checklists
            buttons.insert(0, {
                'label': format_html(
                    '<span style="display: inline-flex; align-items: center; gap: 5px;">'
                    '<span style="font-size: 1.2em;">🔴</span>'
                    '<span>Checklist: {}/{}</span>'
                    '</span>',
                    total_count - incomplete_count, total_count
                ),
                'title': f'{incomplete_count} checklist item(s) incomplete',
                'attrs': {
                    'style': 'background: #ffc107; color: #000; padding: 4px 8px; border-radius: 3px; font-size: 0.85em; font-weight: 600; margin-right: 8px;'
                }
            })
        else:
            # Add success badge with icon for complete checklists
            buttons.insert(0, {
                'label': format_html(
                    '<span style="display: inline-flex; align-items: center; gap: 5px;">'
                    '<span style="font-size: 1.2em;">🟢</span>'
                    '<span>Checklist: {}/{}</span>'
                    '</span>',
                    total_count, total_count
                ),
                'title': 'All checklist items complete',
                'attrs': {
                    'style': 'background: #28a745; color: #fff; padding: 4px 8px; border-radius: 3px; font-size: 0.85em; font-weight: 600; margin-right: 8px;'
                }
            })
    
    return buttons