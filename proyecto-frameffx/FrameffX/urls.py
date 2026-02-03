from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from login.views import LoginFormView, Logout

from users import views
from teachings.api.views import TeachingViewSet, TeachingCRUDView

router = routers.DefaultRouter()
router.register('teachings', TeachingViewSet, basename='teachings')
router.register('teachings-crud', TeachingCRUDView, basename='teachings-crud')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', views.HomeView.as_view(), name='home'),
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout"),

    path('usuarios/create/', views.UsuariosCreateView.as_view(), name='usuarios_create'),
    path('usuarios/update/<int:pk>/', views.UsuariosUpdateView.as_view(), name='usuarios_update'),
    path('usuarios/delete/<int:pk>/', views.UsuariosDeleteView.as_view(), name='usuarios_delete'),
    path('usuarios/', views.UsuariosListView.as_view(), name='usuarios_list'),

    path('accounts/', include('allauth.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
