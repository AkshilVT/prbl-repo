from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # list_display = ('title', 'description', 'completed')
    list_display = ('title', 'completed', 'upload')

# Register your models here.


admin.site.register(Todo, TodoAdmin)
