from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """사용자 프로필 확장 모델"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='사용자')
    phone = models.CharField('전화번호', max_length=20, blank=True)
    bio = models.TextField('소개', blank=True)
    created_at = models.DateTimeField('가입일', auto_now_add=True)
    
    class Meta:
        verbose_name = '프로필'
        verbose_name_plural = '프로필'
    
    def __str__(self):
        return f'{self.user.username}의 프로필'
