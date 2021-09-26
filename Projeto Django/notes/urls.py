from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.noteDelete, name='noteDelete'),
    path('edit/<int:id>', views.noteUpdate, name='noteUpdate'),
    path('tag', views.tagId, name='tagId'),
    path('tag/<int:tagid>', views.tagContent, name='tagContent'),
]