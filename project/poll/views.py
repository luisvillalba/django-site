# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from poll.models import Person, Vote, Poll
from forms import TestForm

def votes(request):
    votes = Vote.objects.order_by('vote_id')
    data = {'votes': votes}
    
    return render(request, 'poll/index.html', context=data)

def form(request):
    data = {'form': TestForm}

    if request.method =='POST':
        form = TestForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['email'])
    
    return render(request, 'poll/form.html', context=data)