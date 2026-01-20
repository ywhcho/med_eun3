from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Board

# Create your views here.

def board_list_view(request):
    boards = Board.objects.all()
    return render(request, 'board/board_list.html', {'boards': boards})

def board_detail_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.views += 1
    board.save()
    return render(request, 'board/board_detail.html', {'board': board})

@login_required
def board_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        Board.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        messages.success(request, '게시글이 작성되었습니다.')
        return redirect('board:list')
    
    return render(request, 'board/board_form.html')

@login_required
def board_edit_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if board.author != request.user:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        messages.success(request, '게시글이 수정되었습니다.')
        return redirect('board:detail', pk=pk)
    
    return render(request, 'board/board_form.html', {'board': board})

@login_required
def board_delete_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if board.author != request.user:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        board.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('board:list')
    
    return render(request, 'board/board_confirm_delete.html', {'board': board})
