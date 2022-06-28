from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from .models import Lost
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_lost_list'

    def get_queryset(self):
        """Return the last five published Lost."""
        return Lost.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Lost
    template_name = 'form.html'

def lostpost(request):
    if request.method == 'POST':
        name = request.POST['name']
        picture = request.POST['picture']
        decription = request.POST['description']
        contact = request.POST['contact']
        lostitem = Lost.objects.create(name = name, picture = picture, decription = decription, contact = contact)
        lostitem.save()
        messages.info(request, '\nPosted as lost item\n')
    return HttpResponseRedirect('index.html')
