from django.shortcuts import render, redirect
from data.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden, HttpResponseNotFound
from data.form import DataForm

def datasets(request):
    datasets = DataSet.objects.all()
    return render(request, 'datasets.html', {'datasets':datasets})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors':authors})

def author(request, id):
    try:
        author = Author.objects.get(id=id)
        ds = DataSet.objects.filter(author=author)
        return render(request, 'author.html', {'author':author, 'datasets':ds})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такого автора нет</h1>")

def dataset(request, id):
    try:
        dataset = DataSet.objects.get(id=id)
        fields = sorted(Field.objects.filter(dataset=dataset), key=lambda x:x.num)
        return render(request, 'dataset.html', {'dataset':dataset, 'fields': fields})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Такого датасета нет</h1>")

def search(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            ds = DataSet.objects.all()
            if form['sciencefields'].value():
                ds = ds.filter(sciencefield__in=form['sciencefields'].value())
            if form['text'].value():
                ds = ds.filter(origname__icontains=form['text'].value())
            if form['fieldtext'].value():
                ds = ds.filter(field__name__icontains=form['fieldtext'].value())
            if form['authors'].value():
                ds = ds.filter(author__in=form['authors'].value())
            return render(request, 'search.html',{'form':form,'datasets':ds})
        else:
            return render(request, 'search.html',{'form':DataForm()})
    return render(request, 'search.html',{'form':DataForm()})


def datasources(request):
    datasources = DataSource.objects.all()
    return render(request, 'datasources.html', {'datasources':datasources})

def datasource(request, id):
    try:
        datasource = DataSource.objects.get(id=id)
        ds = DataSet.objects.filter(datasource=datasource)
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


def newdataset(request, id = None):
    if request.method == 'POST':
        try:
            ds = DataSet.objects.get(id=id)
            form = DataSetForm(request.POST, instance=ds)
        except ObjectDoesNotExist:
            form = DataSetForm(request.POST)
        if form.is_valid():
            nd = form.save()
            return redirect('/dataset/' + str(nd.id))
        return render(request, 'newdataset.html',{'form':form,'error':'Ошибка формы'})
    else:
        try:
            ds = DataSet.objects.get(id=id)
            df = DataSetForm(instance=ds)
        except ObjectDoesNotExist:
            df = DataSetForm()
        return render(request, 'newdataset.html',{'form':df})
    
def newauthor(request, id = None):
    if request.method == 'POST':
        try:
            ds = Author.objects.get(id=id)
            form = AuthorForm(request.POST, instance=ds)
        except ObjectDoesNotExist:
            form = AuthorForm(request.POST)
        if form.is_valid():
            nd = form.save()
            return redirect('/author/' + str(nd.id))
        return render(request, 'newdataset.html',{'form':form,'error':'Ошибка формы'})
    else:
        try:
            ds = Author.objects.get(id=id)
            df = AuthorForm(instance=ds)
        except ObjectDoesNotExist:
            df = AuthorForm()
        return render(request, 'newdataset.html',{'form':df})

def newsciencefield(request, id = None):
    if request.method == 'POST':
        try:
            ds = ScienceField.objects.get(id=id)
            form = ScienceForm(request.POST, instance=ds)
        except ObjectDoesNotExist:
            form = ScienceForm(request.POST)
        if form.is_valid():
            nd = form.save()
            return redirect('/scienceform/' + str(nd.id))
        return render(request, 'newdataset.html',{'form':form,'error':'Ошибка формы'})
    else:
        try:
            ds = ScienceField.objects.get(id=id)
            df = ScienceForm(instance=ds)
        except ObjectDoesNotExist:
            df = ScienceForm()
        return render(request, 'newdataset.html',{'form':df})

def newdatasource(request, id = None):
    if request.method == 'POST':
        try:
            ds = DataSource.objects.get(id=id)
            form = DataSourceForm(request.POST, instance=ds)
        except ObjectDoesNotExist:
            form = DataSourceForm(request.POST)
        if form.is_valid():
            nd = form.save()
            return redirect('/datasource/' + str(nd.id))
        return render(request, 'newdataset.html',{'form':form,'error':'Ошибка формы'})
    else:
        try:
            ds = DataSource.objects.get(id=id)
            df = DataSourceForm(instance=ds)
        except ObjectDoesNotExist:
            df = DataSourceForm()
        return render(request, 'newdataset.html',{'form':df})


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

def gorca(metaid, name):
    d, c = Author.objects.get_or_create(metaid=metaid)
    d.name = name
    d.save()
    return d

def test(request):
    datasource = DataSource.objects.get(id=1)
    for i in range(3000, 3400):
        d = getdataset(i)
        if d is not None:
            scf = gorcscf(d['CategoryId'], d['CategoryCaption'])
            au = gorca(d['DepartmentId'], d['DepartmentCaption'])
            dt = datetime.strptime(d['VersionDate'], '%d.%m.%Y')
            #print(dt)
            dase, fl = DataSet.objects.get_or_create(author=au, size=d['ItemsCount'],lastupdate=dt,origname=d['Caption'],url='https://data.mos.ru/opendata/'+str(d['Id']),datasource=datasource,sciencefield=scf,description=d['FullDescription'] if d['FullDescription'] else d['Description'])
            dase.save()
            for j, field in enumerate(d['Columns']):
                f, fl = Field.objects.get_or_create(name=field['Caption'], num = j, dataset = dase, type=field['Type'])
                f.save()
        print(i)

def index (request):
    return render(request, 'index.html',{})

# Create your views here.
