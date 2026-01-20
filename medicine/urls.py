from django.urls import path
from . import views

app_name = 'medicine'

urlpatterns = [
    path('', views.medicine_list_view, name='list'),
    path('<int:pk>/', views.medicine_detail_view, name='detail'),
    path('ingredient/<str:ingredient>/', views.medicine_by_ingredient_view, name='by_ingredient'),
    path('company/<str:company>/', views.medicine_by_company_view, name='by_company'),
    path('search/', views.medicine_search_view, name='search'),
]
