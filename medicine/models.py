from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=200, verbose_name='약품명')
    ingredient = models.CharField(max_length=200, verbose_name='성분명')
    efficacy = models.TextField(verbose_name='효능')
    dosage = models.CharField(max_length=200, verbose_name='용량')
    precautions = models.TextField(verbose_name='주의사항')
    company = models.CharField(max_length=200, verbose_name='회사명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '의약정보'
        verbose_name_plural = '의약정보'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
