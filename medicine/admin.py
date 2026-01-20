from django.contrib import admin
from .models import Medicine

# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredient', 'company', 'created_at']
    list_filter = ['company', 'ingredient', 'created_at']
    search_fields = ['name', 'ingredient', 'company', 'efficacy']
