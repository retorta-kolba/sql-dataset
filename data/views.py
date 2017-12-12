from django.shortcuts import render, redirect
from data.models import *
from django.core.exceptions import ObjectDoesNotExist
def datasets(request):
    datasets = DataSet.objects.all()
    return render(request, 'datasets.html', {'datasets':datasets})

def dataset(request, id):
    try:
        dataset = DataSet.objects.get(id=id)
        fields = sorted(Field.objects.filter(dataset=dataset), key=lambda x:x.num)
        return render(request, 'dataset.html', {'dataset':dataset, 'fields': fields})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такого датасета нет</h1>")

def datasources(request):
    datasources = DataSource.objects.all()
    return render(request, 'datasources.html', {'datasources':datasources})

def datasource(request, id):
    try:
        datasource = DataSource.objects.get(id=id)
        ds = DataSet.objects.filter(datasource=datasource)
        print(ds)
        return render(request, 'datasource.html', {'datasource':datasource, 'datasets':ds})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такого источника данных нет</h1>")


def sciencefields(request):
    sciencefields = ScienceField.objects.all()
    return render(request, 'sciencefields.html', {'sciencefields':sciencefields})

def sciencefield(request, id):
    try:
        sciencefield = ScienceField.objects.get(id=id)
        ds = DataSet.objects.filter(sciencefield=sciencefield)
        return render(request, 'sciencefield.html', {'sciencefield':sciencefield, 'datasets':ds})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такой области нет</h1>")





from urllib.request import *
import json
from datetime import datetime
api_key = "api_key=35343aed729d9080f3d2fcaf98812838"
def getdataset(_id):
    try:
        a = urlopen("https://apidata.mos.ru/v1/datasets/" + str(_id) + "?" + api_key)
        return json.loads(a.read())
    except:
        return None #json.loads('{}')

def gorcscf(metaid, name=''):
    d, c = ScienceField.objects.get_or_create(metaid=metaid)
    #print(d)
    d.name = name
    d.save()
    return d

def test(request):
    datasource = DataSource.objects.get(id=3)
    for i in range(3300, 3400):
        d = getdataset(i)
        if d is not None:
            scf = gorcscf(d['CategoryId'],d['CategoryCaption'])
            dt = datetime.strptime(d['VersionDate'], '%d.%m.%Y')
            dase, fl = DataSet.objects.get_or_create(size=d['ItemsCount'],lastupdate=dt,origname=d['Caption'],url='https://data.mos.ru/opendata/'+str(d['Id']),datasource=datasource,sciencefield=scf,description=d['FullDescription'] if d['FullDescription'] else d['Description'])
            dase.save()
            for j, field in enumerate(d['Columns']):
                f, fl = Field.objects.get_or_create(name=field['Caption'], num = j, dataset = dase)
                f.save()
        print(i)

def index (request):
    return render(request, 'index.html',{})

# Create your views here.
