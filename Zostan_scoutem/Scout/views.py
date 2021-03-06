from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Club, Player, HAJ, BK, Shortlist
from .forms import PlayerSearchForm, ClubSearchForm, LoginForm, SignupForm, AddToShortForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):

    def get(self, request):
        return render(request, "start.html")


class ClubsView(View):

    def get(self, request):
        form = ClubSearchForm()
        clubs = Club.objects.all().order_by("name")
        return render(request, "clubs.html", {"clubs": clubs, "form": form})


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



@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddClubsView(CreateView):
    model = Club
    fields = '__all__'
    success_url = '/clubs'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
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
        form = AddToShortForm()
        player = get_object_or_404(Player, pk=id)
        return render(request, "playerid1.html", {"player": player, "HAJ":HAJ, "BK":BK, "form":form})

    @method_decorator(login_required(login_url='/login/'), name='dispatch')
    def post(self, request, id):
        form = AddToShortForm(request.POST)
        if form.is_valid():
            player = get_object_or_404(Player, pk=id)
            shortlist_name = form.cleaned_data['shortlist_name']
            for shortlist in shortlist_name:
                shortlist.players.add(player)
                shortlist.save()
            return render(request, "playerid1.html", {"player": player, "HAJ":HAJ, "BK":BK, "form":form})


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddPlayerView(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    success_url = '/players'
    template_name_suffix = "_form"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
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
            user = authenticate(username=username, password=raw_password)
            user.groups.add(group)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'signup.html', {'form': form})


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddShortlistView(CreateView):
    model = Shortlist
    fields = ['shortlist_name', 'loged_user']
    success_url = '/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ShortlistIdView(View):

    def get(self, request, id):
        shorty = get_object_or_404(Shortlist, pk=id)
        return render(request, "shortlistid.html", {"shorty": shorty})


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeleteShortlistView(DeleteView):
    model = Shortlist
    success_url = '/'
    template_name_suffix = "delete_form"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeletePlayerFromShortlistView(View):

    def get(self, request, id_shortlist, id_player):
        player = get_object_or_404(Player, pk=id_player)
        shortlist = get_object_or_404(Shortlist, pk=id_shortlist)
        shortlist.players.remove(player)
        shortlist.save()
        return HttpResponseRedirect(reverse('shortlist_id', args=[id_shortlist]))

