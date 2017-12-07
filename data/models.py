from django.db import models

# Create your models here.
class DataSource(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    url = models.URLField(blank=True)
    def __str__(self):
        return str(self.id) + ' ' + self.name

class ScienceField(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    description = models.TextField(blank=True)
    def __str__(self):
        return str(self.id) + ' ' + self.name

class DataSet(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    lastupdate = models.DateTimeField(auto_now=True)
    origname = models.TextField()
    engname = models.TextField(blank=True)
    url = models.URLField(blank=True)
    datasource = models.ForeignKey(DataSource, related_name='set')
    sciencefield = models.ForeignKey(DataSource, related_name='dataset')
    def __str__(self):
        return str(self.id) + ' ' + self.origname

class Field(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    num = models.IntegerField()
    dataset = models.ForeignKey(DataSet, related_name='field')
    def __str__(self):
        return str(self.id) + ' ' + self.name

