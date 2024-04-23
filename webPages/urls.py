from django.urls import path, include, re_path
from . import views
from webPages.views import index, about, welcome, contacto, exito, flan_detail, search_results
from django.conf.urls import handler404



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('registration/', include('django.contrib.auth.urls')),
    path('flan/<int:flan_id>/', views.flan_detail, name='flan_detail'),
    path('search/', views.search_results, name='search_results'),
    
]

