from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Medicine

# Create your views here.

def medicine_list(request):
    """의약품 전체 목록"""
    medicines = Medicine.objects.all()
    paginator = Paginator(medicines, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/medicine_list.html', {'page_obj': page_obj})

def medicine_detail(request, pk):
    """의약품 상세 정보"""
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicine/medicine_detail.html', {'medicine': medicine})

def by_ingredient(request):
    """성분별 의약품 목록"""
    # 모든 성분 목록 가져오기
    ingredients = Medicine.objects.values_list('ingredient', flat=True).distinct().order_by('ingredient')
    
    # 선택된 성분
    selected_ingredient = request.GET.get('ingredient')
    medicines = None
    
    if selected_ingredient:
        medicines = Medicine.objects.filter(ingredient=selected_ingredient)
        paginator = Paginator(medicines, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = None
    
    context = {
        'ingredients': ingredients,
        'selected_ingredient': selected_ingredient,
        'page_obj': page_obj,
    }
    return render(request, 'medicine/by_ingredient.html', context)

def by_company(request):
    """회사별 의약품 목록"""
    # 모든 회사 목록 가져오기
    companies = Medicine.objects.values_list('company', flat=True).distinct().order_by('company')
    
    # 선택된 회사
    selected_company = request.GET.get('company')
    medicines = None
    
    if selected_company:
        medicines = Medicine.objects.filter(company=selected_company)
        paginator = Paginator(medicines, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = None
    
    context = {
        'companies': companies,
        'selected_company': selected_company,
        'page_obj': page_obj,
    }
    return render(request, 'medicine/by_company.html', context)

def search(request):
    """효능으로 검색"""
    query = request.GET.get('q', '')
    page_obj = None
    
    if query:
        medicines = Medicine.objects.filter(efficacy__icontains=query)
        paginator = Paginator(medicines, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'medicine/search.html', context)
