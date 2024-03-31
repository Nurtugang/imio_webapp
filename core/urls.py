from django.urls import path 
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materials/', views.materials_create_and_list, name='materials_crud'),
    path('materials/select/', views.calculate_with_materials, name='materials_calculate'),
    path('results/all/', views.show_all_results, name='show_all_results'),
    path('update-material/', views.update_material, name='update_material'),
    path('delete-material/<int:material_id>/', views.delete_material, name='delete_material'),
]
