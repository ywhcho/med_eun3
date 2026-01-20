from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Medicine

# Create your views here.

def medicine_list_view(request):
    medicines = Medicine.objects.all()
    
    # Get unique ingredients and companies for filtering
    ingredients = Medicine.objects.values_list('ingredient', flat=True).distinct().order_by('ingredient')
    companies = Medicine.objects.values_list('company', flat=True).distinct().order_by('company')
    
    return render(request, 'medicine/medicine_list.html', {
        'medicines': medicines,
        'ingredients': ingredients,
        'companies': companies,
    })

def medicine_detail_view(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicine/medicine_detail.html', {'medicine': medicine})

def medicine_by_ingredient_view(request, ingredient):
    medicines = Medicine.objects.filter(ingredient=ingredient)
    return render(request, 'medicine/medicine_by_filter.html', {
        'medicines': medicines,
        'filter_type': '성분',
        'filter_value': ingredient
    })

def medicine_by_company_view(request, company):
    medicines = Medicine.objects.filter(company=company)
    return render(request, 'medicine/medicine_by_filter.html', {
        'medicines': medicines,
        'filter_type': '회사',
        'filter_value': company
    })

def medicine_search_view(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.all()
    
    if query:
        medicines = medicines.filter(
            Q(efficacy__icontains=query) |
            Q(name__icontains=query) |
            Q(ingredient__icontains=query)
        )
    
    return render(request, 'medicine/medicine_search.html', {
        'medicines': medicines,
        'query': query
    })
