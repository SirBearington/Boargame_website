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

def topic(request,topic_id): # Here we have the topic_id from urls.py, it helps getting the right topic
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) # get() retireves the topic we have added
    entries = topic.entry_set.order_by('-date_added') #the minus in the 'date-added' sorts the list of topics in reverse order
    context = {'topic': topic, 'entries': entries} #topic and entry get stored inside the context dictionary
    return render(request, 'boardgame_app/topic.html', context) #the context dictionary gets send to the topic.html

# Create your views here.
