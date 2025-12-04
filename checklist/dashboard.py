from wagtail.admin.ui.components import Component
from wagtail.models import Page
from .models import ChecklistItem


class ChecklistSummaryPanel(Component):
    """
    Dashboard panel showing global checklist statistics.
    """
    name = 'checklist_summary'
    template_name = 'checklist/dashboard_summary.html'
    order = 100
    
    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        
        # Get all pages that have checklist items
        pages_with_checklists = Page.objects.filter(
            checklist_items__isnull=False
        ).distinct()
        
        total_pages = pages_with_checklists.count()
        
        # Calculate completed and incomplete
        completed_pages = 0
        incomplete_pages = 0
        
        for page in pages_with_checklists:
            if page.checklist_items.exists():
                incomplete_count = page.checklist_items.filter(is_done=False).count()
                if incomplete_count == 0:
                    completed_pages += 1
                else:
                    incomplete_pages += 1
        
        # Calculate progress percentage
        progress_percentage = 0
        if total_pages > 0:
            progress_percentage = round((completed_pages / total_pages) * 100)
        
        context.update({
            'total_pages': total_pages,
            'completed_pages': completed_pages,
            'incomplete_pages': incomplete_pages,
            'progress_percentage': progress_percentage,
        })
        
        return context
