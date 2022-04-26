from re import search
from django.contrib import admin

#Models
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created')
    list_editable = ('title',)
    list_filter = ('title', 'created', 'updated')
    search_fields = ('title',)
#admin.site.register(Project, ProjectAdmin)