from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Lost
# Create your views here.
def index(request):
    return render(request,'index.html')

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_lost_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Lost.objects.order_by('-pub_date')[:5]

def lostpost(request):
    if request == 'POST':
        return ()
