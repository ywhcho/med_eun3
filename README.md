# 의약정보 관리 시스템 (Medicine Information Management System)

Django 기반 의약품 정보 관리 및 커뮤니티 웹사이트

## 기능 (Features)

### 1. 인증 시스템 (Authentication)
- 회원가입 (User Registration)
- 로그인/로그아웃 (Login/Logout)
- 회원정보 수정 (Profile Edit)

### 2. 게시판 (Board)
- 게시글 작성/수정/삭제 (Create/Edit/Delete Posts)
- 게시글 목록 및 상세보기 (List and Detail View)
- 조회수 추적 (View Count)

### 3. 의약정보 관리 (Medicine Information)
- 의약품 정보: 약품명, 성분명, 효능, 용량, 주의사항, 회사명
- 성분별 의약품 검색 (Search by Ingredient)
- 회사별 의약품 검색 (Search by Company)
- 효능별 의약품 검색 (Search by Efficacy)

### 4. About Us
- 회사 소개 페이지 (의약품 안전사용 전문회사)

## 설치 및 실행 (Installation & Running)

### 1. 필요 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 3. 관리자 계정 생성 (선택사항)
```bash
python manage.py createsuperuser
```

### 4. 개발 서버 실행
```bash
python manage.py runserver
```

웹 브라우저에서 http://127.0.0.1:8000/ 접속

## 테스트 계정 (Test Accounts)

샘플 데이터를 로드하려면 다음 스크립트를 실행하세요:

```python
# create_sample_data.py를 생성하고 실행
python manage.py shell < create_sample_data.py
```

- 관리자: admin / admin123
- 일반사용자: testuser / test1234

## MySQL 설정 (MySQL Configuration)

현재는 개발 편의를 위해 SQLite를 사용하고 있습니다. MySQL로 변경하려면:

1. MySQL 데이터베이스 생성
2. `config/settings.py`의 DATABASES 설정 수정:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'med_eun3',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 프로젝트 구조 (Project Structure)

```
med_eun3/
├── config/          # 프로젝트 설정
├── accounts/        # 회원 관리
├── board/           # 게시판
├── medicine/        # 의약정보 관리
├── pages/           # 정적 페이지 (홈, About)
├── templates/       # HTML 템플릿
├── static/          # 정적 파일 (CSS, JS)
└── manage.py        # Django 관리 스크립트
```

## 기술 스택 (Tech Stack)

- Django 4.2+
- Python 3.8+
- SQLite / MySQL
- HTML/CSS
- Bootstrap-style CSS

## 라이선스 (License)

© 2024 의약품 안전사용 전문회사. All rights reserved.
