from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from .models import LostForm, Lost
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_Lost_list'

    def get_queryset(self):
        """Return the last five published Lost."""
        return Lost.objects.order_by('-pub_date')[:5]

def lostform(request):
    return render(request,'form.html')

def lostpost(request):
    if request.method == 'POST':
        new= Lost()
        form= LostForm(request.POST,request.FILES, instance=new)
        if form.is_valid():
            form.save()
            messages.info(request, '\nPosted as lost item\n')
            return HttpResponseRedirect(reverse('LandF:index',args=(form)))
        else :
            messages.info(request, '\nInvalid Data\n')
    else :
        form = LostForm()
    return render(request, 'form.html', {'form': form})  