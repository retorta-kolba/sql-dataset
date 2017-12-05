from django.contrib import admin

import data.models
# Register your models here.


admin.site.register(data.models.DataSet)
admin.site.register(data.models.Field)