from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home),
    path('signup/', views.Signup),
    path('signin/', views.Signin),
    path('signout/', views.Signout),
    path('booking/', views.Book_Bed),   
    path('account/', views.Account),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
