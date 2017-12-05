from django.db import models

# Create your models here.

class DataSet(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    lastupdate = models.DateTimeField(auto_now=True)
    origname = models.TextField()
    engname = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.id) + ' ' + self.origname

class Field(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField()
    num = models.IntegerField()
    dataset = models.ForeignKey(DataSet, related_name='field')
    def __str__(self):
        return str(self.id) + ' ' + self.name