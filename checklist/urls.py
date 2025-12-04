from django.urls import path
from . import views

app_name = 'checklist'

urlpatterns = [
    path('toggle/<int:item_id>/', views.toggle_checklist_item, name='toggle_item'),
]
