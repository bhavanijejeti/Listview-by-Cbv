from django.shortcuts import render
from django.views.generic import ListView
from app1.models import *
# Create your views here.

class Trainerlist(ListView):
    model=Trainer
    template_name='Trainerlist.html'
    context_object_name='tl'
    #queryset=Trainer.objects.filter(trainer_name='kishore')
    #ordering=['trainer_name']

