from django.core.mail import send_mail
from django.conf import settings
from wagtail.models import Page
from .models import ChecklistItem


def send_checklist_reminders():
    """
    Send email reminders for pages with incomplete checklist items.
    This function can be called manually or scheduled with cron/celery.
    """
    # Get all pages with incomplete checklist items
    pages_with_incomplete = []
    
    all_pages = Page.objects.filter(checklist_items__isnull=False).distinct()
    
    for page in all_pages:
        incomplete_count = page.checklist_items.filter(is_done=False).count()
        if incomplete_count > 0:
            pages_with_incomplete.append({
                'page': page,
                'incomplete_count': incomplete_count,
                'incomplete_items': page.checklist_items.filter(is_done=False)
            })
    
    if not pages_with_incomplete:
        print("No pages with incomplete checklists found.")
        return
    
    # Build email content
    subject = f"⚠️ Checklist Reminder: {len(pages_with_incomplete)} page(s) need attention"
    
    message_lines = [
        "Hello,",
        "",
        f"You have {len(pages_with_incomplete)} page(s) with incomplete checklist items:",
        ""
    ]
    
    for item in pages_with_incomplete:
        page = item['page']
        message_lines.append(f"📄 {page.title} ({item['incomplete_count']} incomplete items)")
        for checklist_item in item['incomplete_items']:
            message_lines.append(f"   ☐ {checklist_item.title}")
        message_lines.append("")
    
    message_lines.extend([
        "Please complete these checklists to publish your content.",
        "",
        "Best regards,",
        "Smart CMS Team"
    ])
    
    message = "\n".join(message_lines)
    
    # Send email
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMINS[0][1]] if settings.ADMINS else ['admin@example.com'],
            fail_silently=False,
        )
        print(f"✅ Reminder email sent successfully for {len(pages_with_incomplete)} page(s).")
        return True
    except Exception as e:
        print(f"❌ Failed to send reminder email: {e}")
        return False


def get_incomplete_pages_summary():
    """
    Get a summary of all pages with incomplete checklists.
    Useful for reporting and analytics.
    """
    summary = []
    
    all_pages = Page.objects.filter(checklist_items__isnull=False).distinct()
    
    for page in all_pages:
        total_items = page.checklist_items.count()
        incomplete_count = page.checklist_items.filter(is_done=False).count()
        
        if incomplete_count > 0:
            summary.append({
                'page_id': page.id,
                'page_title': page.title,
                'total_items': total_items,
                'incomplete_count': incomplete_count,
                'completion_percentage': round(((total_items - incomplete_count) / total_items) * 100)
            })
    
    return summary
