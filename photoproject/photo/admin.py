from django.contrib import admin

# Register your models here.
from .models import Categoty, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

admin.site.register(Categoty, CategoryAdmin)
admin.site.register(PhotoPost, PhotoPostAdmin)