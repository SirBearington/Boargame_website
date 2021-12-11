from django.shortcuts import render

def index(request):
    """The home page for Boardgame website."""
    return render(request, 'boardgame_app/index.html')

# Create your views here.
