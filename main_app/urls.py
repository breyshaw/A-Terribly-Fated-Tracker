from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('masks/', views.masks_index, name='masks_index'),
  path('masks/<int:mask_id>/', views.masks_detail, name='masks_detail'),
  path('files/', views.files_index, name='files_index'),
  path('files/<int:file_id>/', views.files_detail, name='files_detail'),
  path('files/create/', views.FileCreate.as_view(), name='files_create'),
  path('files/create/', views.FileCreate.as_view(), name='files_create'),
  path('files/<int:pk>/update/', views.FileUpdate.as_view(), name='files_update'),
  path('files/<int:pk>/delete/', views.FileDelete.as_view(), name='files_delete'),
  path('files/<int:file_id>/assoc_mask/<int:mask_id>/', views.assoc_mask, name='assoc_mask'),
  path('files/<int:file_id>/remove_mask/<int:mask_id>/', views.remove_mask, name='remove_mask'),
]