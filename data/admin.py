from django.contrib import admin

import data.models
# Register your models here.


admin.site.register(data.models.DataSet)
admin.site.register(data.models.Field)
admin.site.register(data.models.DataSource)
admin.site.register(data.models.ScienceField)
admin.site.register(data.models.Author)