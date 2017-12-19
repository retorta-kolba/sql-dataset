from django.db import models
from django.forms import ModelForm

# Create your models here.
class DataSource(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField()
    url = models.URLField(blank=True)
    def __str__(self):
        return str(self.id) + ' ' + self.name

class ScienceField(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    description = models.TextField(blank=True)
    metaid = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.id) + ' ' + self.name

class Author(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    contacts = models.TextField(blank=True, null=True)
    metaid = models.IntegerField(blank=True, null=True)
    sources = models.ManyToManyField(DataSource, related_name='authors')
    def __str__(self):
        return str(self.id) + ' ' + self.name

class DataSet(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    size = models.IntegerField(blank=True, null=True)
    lastupdate = models.DateTimeField()
    author = models.ForeignKey(Author, models.CASCADE, related_name='dataset')
    origname = models.TextField()
    engname = models.TextField(blank=True)
    url = models.URLField(blank=True)
    datasource = models.ForeignKey(DataSource, models.CASCADE, related_name='set')
    sciencefield = models.ForeignKey(ScienceField, models.CASCADE, related_name='dataset')
    description = models.TextField(blank=True)
    def __str__(self):
        return str(self.id) + ' ' + self.origname

class Field(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    num = models.IntegerField()
    dataset = models.ForeignKey(DataSet, models.CASCADE, related_name='field')
    type = models.TextField()
    def __str__(self):
        return str(self.id) + ' ' + self.name


class DataSourceForm(ModelForm):
    class Meta:
        model = DataSource
        fields = ['id', 'name', 'url']

class ScienceForm(ModelForm):
    class Meta:
        model = ScienceField
        fields = ['id', 'name', 'description']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['id', 'name', 'contacts','sources']

class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ['id', 'name', 'num', 'dataset']

class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        fields = ['id', 'origname', 'author', 'datasource','sciencefield','lastupdate','size','url','description']
