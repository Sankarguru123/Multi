from django.contrib import admin
from . models import Task


class AdminTask(admin.ModelAdmin):

    list_display = ("user",'title','description','created')
    list_filter = ('title','user','complete')
admin.site.register(Task,AdminTask)
admin.site.site_header = 'V2Soft'
