from django.contrib.auth.decorators import login_required
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


class AddView(generic.ListView):
    template_name = 'add.html'
    context_object_name = 'threads'

    def get_queryset(self):
        return Thread.objects.order_by('-date')


# class AddView(generic.DetailView):
#     model = Thread
#     template_name = 'detail.html'

@login_required
def new(request):

    new_thread = Thread(
        name=request.POST["subject"],
        description=request.POST["description"],
        author=request.user,
    )
    new_thread.save()
    return HttpResponseRedirect(reverse('forum:index'))
