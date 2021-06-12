from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
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

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super(DetailView, self).get_context_data(**kwargs)

        if not request.POST["comment"]:
            context["error"] = True
            context["message"] = "Please fill comment field."
            return self.render_to_response(context=context)

        new_message = Message(
            author=request.user,
            thread=self.object,
            message=request.POST["comment"],
        )
        new_message.save()
        return self.render_to_response(context=context)


class AddView(generic.TemplateView):
    template_name = 'add.html'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        context = super(AddView, self).get_context_data(**kwargs)

        if not request.POST["subject"] or not request.POST["description"]:
            context["error"] = True
            context["message"] = "Please fill all fields."
            return self.render_to_response(context=context)

        new_thread = Thread(
            name=request.POST["subject"],
            description=request.POST["description"],
            author=request.user,
        )
        # Author of the thread is a voter
        new_thread.save()
        new_thread.voters.add(request.user)
        return HttpResponseRedirect(reverse('forum:index'))

@login_required
def vote(request, thread_id):

    thread = get_object_or_404(Thread, pk=thread_id)

    # Author can't remove his vote
    if not thread.author == request.user:
        # Remove or add vote
        if request.user in thread.voters.all():
            thread.voters.remove(request.user)
        else:
            thread.voters.add(request.user)

    return HttpResponseRedirect(reverse('forum:index'))
