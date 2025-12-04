from django.contrib import admin
from .models import ChecklistItem

@admin.register(ChecklistItem)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "is_done")

# Register your models here.
