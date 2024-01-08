from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'developer', 'release_date')
    list_filter = ('category', 'subcategory', 'developer', 'release_date')
    search_fields = ('name', 'description', 'developer')
    prepopulated_fields = {'slug': ('name',)}
    # Additional customization options can be added here
