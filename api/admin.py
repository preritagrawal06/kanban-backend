from django.contrib import admin
from .models import Todo, Project, Column

class TodoAdmin(admin.ModelAdmin):
    pass

class ColumnAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Column, ColumnAdmin)