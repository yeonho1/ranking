# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Ranker
from .forms import RankerForm

# Create your views here.

def viewRanking(request):
    ranking = Ranker.objects.all().order_by('rank')
    return render(request, 'rank/view.html', {'ranking' : ranking})


def editRanking(request, id):
    ranker = get_object_or_404(Ranker, id=id)
    if request.method == 'POST':
        form = RankerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rank = form.cleaned_data['rank']
            additions = form.cleaned_data['additions']
            ranker.name = name
            ranker.rank = rank
            ranker.additions = additions
            ranker.save()
            return render(request, 'rank/success.html', {'name': name, 'rank': rank, 'additions': additions})
    else:
        #form = RankerForm(instance=ranker)
        form = RankerForm(initial={'name': ranker.name, 'rank': ranker.rank, 'additions': ranker.additions},label_suffix='')
        return render(request, 'rank/edit.html', {'form': form})
    
def viewEdit(request):
    ranking = Ranker.objects.all().order_by('rank')
    return render(request, 'rank/editView.html', {'ranking': ranking})

def editAllRanking(request):
    rankers = Ranker.objects.all().order_by('rank')
    forms = []
    for ranker in rankers:
        forms.append({'form': RankerForm(initial={'name': ranker.name, 'rank': ranker.rank, 'additions' : ranker.additions}, label_suffix=''), 'id': ranker.id, 'name': ranker.name})
    return render(request, 'rank/allEdit.html', {'forms': forms})

def rEdit(request, id):
    ranker = get_object_or_404(Ranker, id=id)
    if request.method == 'POST':
        form = RankerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rank = form.cleaned_data['rank']
            additions = form.cleaned_data['additions']
            ranker.name = name
            ranker.rank = rank
            ranker.additions = additions
            ranker.save()
            return redirect('editall')
    else:
        return redirect('editall')

def addRanker(request):
    if request.method == 'POST':
        form = RankerForm(request.POST)
        if form.is_valid():
            ranker = Ranker(name=form.cleaned_data['name'], rank=form.cleaned_data['rank'], additions=form.cleaned_data['additions'])
            ranker.save()
            return redirect('main')
    else:
        form = RankerForm()
        return render(request, 'rank/add.html', {'form': form})

def delete(request, id):
    ranker = Ranker.objects.get(id=id)
    ranker.delete()
    return redirect('main')

def deleteView(request):
    rankers = Ranker.objects.all().order_by('rank')
    return render(request, 'rank/delete.html', {'rankers': rankers})