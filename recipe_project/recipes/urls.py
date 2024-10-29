from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('new/', views.recipe_create, name='recipe_create'),
    path('recipe/<slug:slug>/edit/', views.recipe_update, name='recipe_update'),
    path('recipe/<slug:slug>/delete/', views.recipe_delete, name='recipe_delete'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
]
