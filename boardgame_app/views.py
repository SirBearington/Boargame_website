from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Boardgame website."""
    return render(request, 'boardgame_app/index.html')
    
@login_required
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

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = TopicForm()
    else:
    # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boardgame_app:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'boardgame_app/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('boardgame_app:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'boardgame_app/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boardgame_app:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'boardgame_app/edit_entry.html', context)

# Create your views here.
