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
        return HttpResponseNotFound("<h1>Такого датасета нет</h1>")

def datasources(request):
    datasources = DataSource.objects.all()
    return render(request, 'datasources.html', {'datasources':datasources})

def datasource(request, id):
    try:
        datasource = DataSource.objects.get(id=id)
        return render(request, 'datasource.html', {'datasource':datasource})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такого источника данных нет</h1>")


def sciencefields(request):
    sciencefields = ScienceField.objects.all()
    return render(request, 'sciencefields.html', {'sciencefields':sciencefields})

def sciencefield(request, id):
    try:
        sciencefield = ScienceField.objects.get(id=id)
        return render(request, 'sciencefield.html', {'sciencefield':sciencefield})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такой области нет</h1>")

def test(request):
    pass

def index (request):
    return render(request, 'index.html',{})

# Create your views here.
