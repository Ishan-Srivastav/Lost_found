from django import forms
from django.db import models
from django.utils import timezone
import datetime

from pkg_resources import require

# Create your models here.

class Lost(models.Model):
    picture = models.ImageField(upload_to = 'media', default='None')
    
    # TYPE_OF_LOST={
    #     ('ID','ID'),
    #     ('EL','Electronics'),
    #     ('OT','Other')
    # }
    # Type = models.CharField(
    #     max_length= 2,
    #     choices= TYPE_OF_LOST,
    #     default= 'OT',
    # )

    name = models.CharField(max_length= 15, default='None')
    description = models.CharField(max_length= 200, default= 'None')
    contact = models.CharField(max_length= 100, default='None')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = '__all__'

