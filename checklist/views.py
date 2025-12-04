from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import ChecklistItem

@require_POST
@csrf_exempt  # We'll handle CSRF via Wagtail's built-in protection
def toggle_checklist_item(request, item_id):
    """
    Toggle the is_done status of a checklist item.
    """
    try:
        item = ChecklistItem.objects.get(id=item_id)
        item.is_done = not item.is_done
        item.save()
        
        return JsonResponse({
            'success': True,
            'is_done': item.is_done,
            'item_id': item.id
        })
    except ChecklistItem.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Checklist item not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
