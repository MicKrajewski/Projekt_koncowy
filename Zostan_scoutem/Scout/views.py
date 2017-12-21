from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Club, Player, HAJ, BK, Shortlist
from .forms import PlayerSearchForm, ClubSearchForm, LoginForm, SignupForm, AddToShortForm, ShortlistForm


class HomeView(View):
    def get(self, request):
        return render(request, "start.html")


class ClubsView(PermissionRequiredMixin, View):

    permission_required = "Scout.add_club"

    def get(self, request):
        form = ClubSearchForm()
        clubs = Club.objects.all().order_by("name")
        return render(request, "clubs.html", {"clubs": clubs, "form": form})

    def post(self, request):
        if request.user.has_perm("add_club"):
            form = ClubSearchForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                result = Club.objects.filter(name__icontains=name)
            # else:
            #     return render(request, "clubs.html", {"form": ClubSearchForm(), "msg": "Nie ma takiego klubu w bazie"})
            return render(request, "clubs.html", {"form": form, "result": result})
        else:
            return HttpResponse("Nie da się!")


class SearchClubView(View):

    def get(self, request):
        form = ClubSearchForm()
        clubs = Club.objects.all().order_by("name")
        return render(request, "search-club.html", {"clubs":clubs, "form": form})

    def post(self, request):
        form = ClubSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            result = Club.objects.filter(name__icontains=name)
        # else:
        #     return render(request, "players.html", {"form": PlayerSearchForm(), "msg": "Nie ma takiego piłkarza w bazie"})
        return render(request, "search-club.html", {"form": form, "result": result})


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
        form = PlayerSearchForm()
        players = Player.objects.all().order_by("last_name")
        return render(request, "players.html", {"players": players, "form": form})


class SearchPlayerView(View):

    def get(self, request):
        form = PlayerSearchForm()
        players = Player.objects.all().order_by("last_name")
        return render(request, "search-player.html", {"players": players, "form": form})

    def post(self, request):
        form = PlayerSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            result = Player.objects.filter(last_name__icontains=name)
        # else:
        #     return render(request, "players.html", {"form": PlayerSearchForm(), "msg": "Nie ma takiego piłkarza w bazie"})
        return render(request, "search-player.html", {"form": form, "result": result})



class PlayerIdView(View):
    def get(self, request, id):
        player = get_object_or_404(Player, pk=id)
        return render(request, "playerid1.html", {"player": player, "HAJ":HAJ, "BK":BK})

    def post(self, request, id):
        form = AddToShortForm(request.POST)
        if form.is_valid():
            pass



class AddPlayerView(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players'


class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    success_url = '/players'
    template_name_suffix = "_form"


class ListUsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "list-users.html", {"users": users})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "form_show.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth = authenticate(username=username, password=password)
            if auth:
                login(request, auth)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
        return render(request, "form_show.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')


class SignupView(View):

    def get(self, request):
        form = SignupForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password1"]
            group = form.cleaned_data["group"]
            user = authenticate(username=username, password=raw_password, group=group)
            login(request, user)
            return HttpResponseRedirect(reverse('/'))
        return render(request, 'signup.html', {'form': form})


class AddShortlistView(CreateView):
    model = Shortlist
    fields = ['shortlist_name', 'loged_user']
    success_url = '/shortlist'


class ShortlistView(View):

    def get(self, request):
        # form = ShortlistForm()
        shorty = Shortlist.objects.all()
        # players = Player.objects.filter(clubs=club)
        return render(request, "shortlist.html", {"shorty": shorty})

class AddToShort(View):

    def get(self, request, id, short_id):
        player = get_object_or_404(Player, pk=id)
        shortlist = get_object_or_404(Shortlist, pk=short_id)
        return render(request, "shortlist.html", {"shortlist": shortlist, "player":player})

