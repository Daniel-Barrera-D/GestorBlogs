from asyncore import read
from re import search
from django.contrib import admin

#Models
from .models import Blogs

# Register your models here.
#admin.site.register(Blogs)

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description', 'created')
    list_display_links = ('title',)
    list_filter = ('created', 'updated')
    search_fields = ('title', 'description')
    readonly_fields = ('created', 'updated')