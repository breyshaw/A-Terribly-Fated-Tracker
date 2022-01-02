from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('masks/', views.masks_index, name='masks_index'),
  path('masks/<int:mask_id>/', views.masks_detail, name='masks_detail'),
  path('files/', views.files_index, name='files_index'),
  path('files/<int:file_id>/', views.files_detail, name='files_detail'),
]