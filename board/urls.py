from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list_view, name='list'),
    path('<int:pk>/', views.board_detail_view, name='detail'),
    path('create/', views.board_create_view, name='create'),
    path('<int:pk>/edit/', views.board_edit_view, name='edit'),
    path('<int:pk>/delete/', views.board_delete_view, name='delete'),
]
