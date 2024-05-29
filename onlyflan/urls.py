from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from onlyflan_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
