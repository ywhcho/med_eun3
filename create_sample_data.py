"""
Sample data creation script for med_eun3 project.
Run with: python manage.py shell < create_sample_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from medicine.models import Medicine
from board.models import Board

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✓ Superuser created: admin/admin123')
else:
    print('✓ Superuser already exists')

# Create test user
if not User.objects.filter(username='testuser').exists():
    User.objects.create_user('testuser', 'test@example.com', 'test1234')
    print('✓ Test user created: testuser/test1234')
else:
    print('✓ Test user already exists')

# Create sample medicines
medicines_data = [
    {
        'name': '타이레놀',
        'ingredient': '아세트아미노펜',
        'efficacy': '해열, 진통',
        'dosage': '1회 500mg, 1일 3-4회',
        'precautions': '간질환 환자 주의, 알코올과 함께 복용 금지',
        'company': '한국얀센'
    },
    {
        'name': '게보린',
        'ingredient': '아세트아미노펜',
        'efficacy': '두통, 치통, 발열',
        'dosage': '1회 1-2정, 1일 3-4회',
        'precautions': '임산부 주의',
        'company': '삼진제약'
    },
    {
        'name': '아스피린',
        'ingredient': '아세틸살리실산',
        'efficacy': '해열, 진통, 항염',
        'dosage': '1회 500mg-1g, 1일 3-4회',
        'precautions': '위장장애 주의, 출혈성 질환 금기',
        'company': '바이엘'
    },
    {
        'name': '부루펜',
        'ingredient': '이부프로펜',
        'efficacy': '소염진통제, 해열',
        'dosage': '1회 200-400mg, 1일 3-4회',
        'precautions': '위장장애 가능, 천식환자 주의',
        'company': '삼일제약'
    },
    {
        'name': '애드빌',
        'ingredient': '이부프로펜',
        'efficacy': '두통, 생리통, 근육통',
        'dosage': '1회 200mg, 1일 3-4회',
        'precautions': '신장질환 환자 주의',
        'company': '화이자'
    },
    {
        'name': '판피린',
        'ingredient': '아세트아미노펜',
        'efficacy': '감기로 인한 발열 및 통증 완화',
        'dosage': '1회 2정, 1일 3회',
        'precautions': '간질환, 신장질환 환자 주의',
        'company': '동아제약'
    },
    {
        'name': '펜잘',
        'ingredient': '이부프로펜',
        'efficacy': '소염, 진통, 해열',
        'dosage': '1회 1정, 1일 2-3회',
        'precautions': '위장장애 주의',
        'company': '한국화이자'
    },
]

for med_data in medicines_data:
    if not Medicine.objects.filter(name=med_data['name']).exists():
        Medicine.objects.create(**med_data)
        print(f"✓ Medicine created: {med_data['name']}")
    else:
        print(f"✓ Medicine already exists: {med_data['name']}")

# Create sample board posts
admin_user = User.objects.get(username='admin')
boards_data = [
    {
        'title': '의약품 안전사용 안내',
        'content': '''의약품을 안전하게 사용하기 위한 기본 수칙을 안내드립니다.

1. 의사, 약사의 지시대로 복용하세요
2. 복용량과 복용시간을 정확히 지키세요
3. 다른 약과의 병용 시 전문가와 상담하세요
4. 약물 알레르기가 있는 경우 반드시 알려주세요
5. 임신 중이거나 수유 중인 경우 전문가와 상담하세요''',
        'author': admin_user
    },
    {
        'title': '일반의약품과 전문의약품의 차이',
        'content': '''일반의약품과 전문의약품의 차이점을 설명드립니다.

일반의약품: 
- 약국에서 처방전 없이 구매 가능
- 상대적으로 안전성이 높은 의약품
- 예) 타이레놀, 게보린 등

전문의약품:
- 의사의 처방전이 필요한 의약품
- 전문가의 관리가 필요한 의약품
- 부작용 위험이 상대적으로 높음''',
        'author': admin_user
    },
    {
        'title': '진통제 복용 시 주의사항',
        'content': '''진통제를 복용할 때는 다음 사항을 주의해야 합니다.

1. 공복에 복용하지 마세요
2. 알코올과 함께 복용하지 마세요
3. 장기간 복용하지 마세요
4. 여러 진통제를 동시에 복용하지 마세요
5. 부작용이 나타나면 즉시 복용을 중단하고 전문가와 상담하세요''',
        'author': admin_user
    },
]

for board_data in boards_data:
    if not Board.objects.filter(title=board_data['title']).exists():
        Board.objects.create(**board_data)
        print(f"✓ Board post created: {board_data['title']}")
    else:
        print(f"✓ Board post already exists: {board_data['title']}")

print('\n✅ Sample data creation completed!')
print('\nTest accounts:')
print('  - Admin: admin/admin123')
print('  - User: testuser/test1234')
