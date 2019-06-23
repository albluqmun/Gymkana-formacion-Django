from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from .models import New, Event
from .forms import NewNews


def index(request):
    latest_news_list = New.objects.order_by('-id')[:3]
    latest_events_list = Event.objects.order_by('-id')[:3]
    context = {
        'latest_news_list': latest_news_list,
        'latest_events_list': latest_events_list,
    }
    return render(request, 'blog/index.html', context)


def news_create(request):
    form = NewNews()
    if request.method == 'POST':
        form = NewNews(request.POST, request.FILES)
        if form.is_valid():
            print ("form was valid TEST")
            post = form.save(commit=False)
            post.publish_date = timezone.now()
            post.save()
    return render(request, 'blog/post_create.html', {'form': form})
