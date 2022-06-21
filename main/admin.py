from django.contrib import admin
from main.models import *
# Register your models here.

class AdminContent(admin.ModelAdmin):
    pass
admin.site.register(Content,AdminContent)



class AdminName(admin.ModelAdmin):
    pass
admin.site.register(Name,AdminName)