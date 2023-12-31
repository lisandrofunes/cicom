from django import views
from django.contrib import admin

from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    #  path('', CargarArchivoView.as_view(), name='cargar_archivo'),
    path('create/', views.ArchivoCreate.as_view(), name='archivo-create'),
    path('', views.index, name='index'),
    path('archivos/', views.ArchivoListView.as_view(), name='archivo-list'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)