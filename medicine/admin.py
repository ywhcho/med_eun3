from django.contrib import admin
from .models import Medicine

# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['drug_name', 'ingredient', 'company', 'created_at']
    list_filter = ['ingredient', 'company', 'created_at']
    search_fields = ['drug_name', 'ingredient', 'company', 'efficacy']
    date_hierarchy = 'created_at'
