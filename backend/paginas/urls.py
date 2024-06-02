from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home.html', views.home),
    path('contact.html', views.contact),
    path('overSBWE.html', views.Over),
    path('historie.html', views.historie),
    path('atelier.html', views.atelier),

    #CC:
    path('CC/verhuurBK.html', views.verhuurBK),
    path('CC/reserveringBK.html', views.reserveringBK),
    path('CC/voorwaardenBK.html', views.voorwaardenBK),
    path('CC/impressieBK.html', views.impressieBK),

    #panden:
    path('panden/panden.html', views.panden),
    path('panden/barthkapel.html', views.gebouwBK),
    path('panden/looyerstr.html', views.gebouwLO),


    path('post_list.html/', views.post_list, name = 'post_list'),
    ]

