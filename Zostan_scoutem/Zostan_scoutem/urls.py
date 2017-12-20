"""Zostan_scoutem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Scout.views import (ClubsView, ClubIdView, AddClubsView, ClubUpdateView, PlayersView, PlayerIdView, AddPlayerView,
                         PlayerUpdateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/', ClubsView.as_view(), name="clubs"),
    path('club/<int:id>/', ClubIdView.as_view(), name="club_id"),
    path('add-club/', AddClubsView.as_view(), name="add_club"),
    path('update-club/<int:pk>/', ClubUpdateView.as_view(), name="update_club"),
    path('players/', PlayersView.as_view(), name="players"),
    path('player/<int:id>/', PlayerIdView.as_view(), name="player_id"),
    path('add-player/', AddPlayerView.as_view(), name="add_player"),
    path('update-player/<int:pk>/', PlayerUpdateView.as_view(), name="update_player"),

]
