from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import LostForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_lost_list'

    def get_queryset(self):
        """Return the last five published Lost."""
        return Lost.objects.order_by('-pub_date')[:5]

def lostform(request):
    return render(request,'form.html')

def lostpost(request):
    if request.method == 'POST':
        name = request.POST['name']
        picture = LostForm(request.POST, request.FILES)
        decription = request.POST['description']
        contact = request.POST['contact']
        lostitem = Lost.objects.create(name = name, picture = picture, decription = decription, contact = contact)
        if picture.is_valid():
            lostitem.save()
            messages.info(request, '\nPosted as lost item\n')
        return HttpResponseRedirect('index.html')
    else :
        form = LostForm()
    return render(request, 'form.html', {'form': form})  