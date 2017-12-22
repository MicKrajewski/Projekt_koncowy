from .models import Shortlist

def my_cp(request):

    short = Shortlist.objects.all()
    ctx = {"short": short}
    return ctx