import os

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import (ListView, UpdateView)

from .forms import EventForm
from .models import Event


# Create your views here.
def index(request):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    newspaper_email = os.path.join(THIS_FOLDER, 'email.txt')
    with open(newspaper_email, 'r', encoding="utf8") as f:
        newspaper = f.read()
    newspaper = mark_safe(newspaper)
    return render(request, 'email_parser/index.html', {'newspaper': newspaper})


class EventListView(ListView):
    model = Event
    template_name = 'email_parser/event_list.html'


class UpdateEventView(UpdateView):
    form_class = EventForm
    model = Event

    # def test_func(self):
    #   return self.request.user.is_superuser
