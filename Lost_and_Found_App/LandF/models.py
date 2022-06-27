from pickle import TRUE
from typing_extensions import Required
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
import datetime

# Create your models here.

class lost(models.Model):
    picture = models.ImageField(upload_to = 'media')
    
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

    name = models.CharField(max_length= 15, required= True)
    description = models.CharField(max_length= 200)
    contact = models.CharField(max_length= 100, required = True)
    def __str__(self):
        return self.name

