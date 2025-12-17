from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.recipe_create, name='recipe_create'),
    path('<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('search/', views.recipe_list, name='search_results'), # Search logic handled in list view or separate view
]
