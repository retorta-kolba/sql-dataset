from django.shortcuts import render, redirect
from data.models import *

def datasets(request):
    datasets = DataSet.objects.all()
    return render(request, 'datasets.html', {'datasets':datasets})

def dataset(request, id):
    try:
        dataset = DataSet.objects.get(id=id)
        return render(request, 'dataset.html', {'dataset':dataset})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такого программиста нет</h1>")

def test(request):
    pass
# Create your views here.
