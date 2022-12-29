from django.shortcuts import redirect
from django.urls import path
from . import views
urlpatterns = [
    path('', views.maison,),
    path('home/', views.accueil, name='home'),
    path('home/<genre>', views.categorie, name='genre'),
    path('home/<int:id>/', views.page_serie, name='page_serie'),
    path('redirect/<genre>', views.rediriger_accueil, name='redirect'),
    path('home/<int:id>/<int:il>/', views.page_epi, name='page_episode'),
    path('home/<int:id>/<int:il>/<syntax>/', views.redirect_epi, name='redirect_epi'),
    path('home/tout/', views.voir_tout, name='tout'),
    path('redirect_serie/<int:id>', views.rediriger_serie, name='redirect_serie'),
    path('home/agenda/', views.agenda, name='agenda'),
    path('ajax/', views.recherche_ajaz, name='ajax'),
    path('ajax/<int:id>', views.ajax_redirect, name='ajax_redirect'),
    path('addwatch/', views.watchlist, name='add_watch'),
    
    


]