from django.shortcuts import render
# from newsdigester.celery import debug_task
# from .tasks import fetch_feeds

# Create your views here.
def index(request):
    # fetch_feeds.delay()
    return render(request, "index.html")