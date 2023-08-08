from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register(Contact)
admin.site.register(BannerImages)
class Projects_DataAdmin(admin.ModelAdmin):
    list_display = ["project_name", "project_details", "project_images","project_links"]
    
    
    

admin.site.register(Projects_Data,Projects_DataAdmin)    
    