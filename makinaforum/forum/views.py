from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Thread, Message


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'threads'

    def get_queryset(self):
        return Thread.objects.order_by('-date')


class DetailView(generic.DetailView):
    model = Thread
    template_name = 'detail.html'



