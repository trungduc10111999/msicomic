from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from comic import views
from profiles import views as profiles_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home_view, name='home'),
    path('OverView/', profiles_views.SiteOverView, name='OverView'),
    path('18+/', views.up18_view, name='18+'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('login/', profiles_views.loginView.as_view(), name='login'),
    path('register/', profiles_views.RegisterView.as_view(), name='register'),
    path('register/ok/', profiles_views.SiteRegisterOk.as_view(), name='register_ok'),
    path('logout/', profiles_views.SiteLogOut.as_view(), name='logout'),

    path('profile/', profiles_views.ProfileEditView.as_view(), name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

