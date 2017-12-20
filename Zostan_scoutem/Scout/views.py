from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Club, Player, HAJ, BK
from .forms import ClubsForm


class ClubsView(View):

    def get(self, request):
        clubs = Club.objects.all().order_by("name")
        return render(request, "clubs.html", {"clubs": clubs})


class ClubIdView(View):
    def get(self, request, id):
        club = get_object_or_404(Club, pk=id)
        players = Player.objects.filter(clubs=club)
        return render(request, "clubid.html", {"club": club, "players":players})


class AddClubsView(CreateView):
    model = Club
    fields = '__all__'
    success_url = '/clubs'


class ClubUpdateView(UpdateView):
    model = Club
    fields = '__all__'
    success_url = '/clubs'
    template_name_suffix = "_form"


class PlayersView(View):

    def get(self, request):
        players = Player.objects.all().order_by("last_name")
        return render(request, "players.html", {"players": players})


class PlayerIdView(View):
    def get(self, request, id):
        player = get_object_or_404(Player, pk=id)
        return render(request, "playerid.html", {"player": player, "HAJ":HAJ, "BK":BK})


class AddPlayerView(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players'


class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    success_url = '/players'
    template_name_suffix = "_form"