from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
]

#check if we are in debug mode before serving static files
urlpatterns += staticfiles_urlpatterns()
