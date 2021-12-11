from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Boardgame website."""
    return render(request, 'boardgame_app/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'boardgame_app/topics.html', context)


# Create your views here.
