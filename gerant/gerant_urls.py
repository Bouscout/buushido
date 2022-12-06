from django.shortcuts import redirect
from django.urls import path
from . import views
urlpatterns = [
    path('', views.accueil_gerant, name='gerant_accueil'),
    path('onglet/<int:id>/', views.edit_onglet, name='onglet_edit'),
    path('onglet/', views.create_onglet, name='onglet'),
    path('onglet/diffuse/', views.diffuser, name='diffusion'),
    path('serie/', views.poster_video, name='nouvelle_serie'),
    path('serie/<int:id>/', views.ajouter_plusieurs_episode, name='new_episodes'),
    path('serie/<int:id>/<int:il>/', views.modifier_lien, name='modifier_lien'),
    path('serie/plusieurs/<int:id>/', views.plusieurs_episodes, name='plusieurs'),
    path('edit/<int:id>/', views.modifier_serie, name='modifier_serie'),
    path('edit/<int:id>/epi/', views.supprim_episode, name='supprimer_epi'),


]