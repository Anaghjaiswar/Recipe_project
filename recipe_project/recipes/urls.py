from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import change_password


urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('change-password/', change_password, name='change_password'),
    path('logout/done/', auth_views.LogoutView.as_view(template_name='recipes/logout.html'), name='logout'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('new/', views.recipe_create, name='recipe_create'),
    path('recipe/<slug:slug>/edit/', views.recipe_update, name='recipe_update'),
    path('recipe/<slug:slug>/delete/', views.recipe_delete, name='recipe_delete'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)