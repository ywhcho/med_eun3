from django.contrib import admin
from .models import Board

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
