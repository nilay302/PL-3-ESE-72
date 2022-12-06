from django.contrib import admin
from . import models
# Register your models here.
class BonafideAdmin(admin.ModelAdmin):
    list_display = ('Name',)#To show the title name in admin site

admin.site.register(models.Bonafide,BonafideAdmin)