# med_eun3

Django 기반 의약품 안전사용 정보 시스템

## 주요 기능

### 1. 사용자 인증
- 회원가입 / 로그인 / 로그아웃
- 사용자 프로필 보기 및 수정

### 2. 게시판
- 게시글 작성, 수정, 삭제
- 게시글 목록 조회 (페이징)
- 조회수 카운트

### 3. 의약정보 관리
- **전체 목록**: 모든 의약품 조회
- **성분별 보기**: 성분별로 의약품 검색
- **회사별 보기**: 제약회사별로 의약품 검색
- **효능 검색**: 효능 키워드로 의약품 검색

### 4. About Us
- 회사 소개 페이지

## 설치 방법

### 1. 저장소 클론
```bash
git clone https://github.com/ywhcho/med_eun3.git
cd med_eun3
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 5. 샘플 데이터 생성 (선택사항)
```bash
python manage.py create_sample_medicines
```

### 6. 관리자 계정 생성 (선택사항)
```bash
python manage.py createsuperuser
```

### 7. 서버 실행
```bash
python manage.py runserver
```

브라우저에서 http://localhost:8000 접속

## 기술 스택

- **Backend**: Django 6.0.1
- **Database**: SQLite (개발용), MySQL 지원
- **Frontend**: Bootstrap 5, HTML, CSS
- **Language**: Python 3.12+

## 프로젝트 구조

```
med_eun3/
├── accounts/          # 사용자 인증 앱
├── board/            # 게시판 앱
├── medicine/         # 의약품 정보 앱
├── pages/            # 정적 페이지 앱 (홈, About)
├── templates/        # 공통 템플릿
├── med_eun3_project/ # 프로젝트 설정
└── manage.py
```

## 데이터베이스 모델

### Medicine (의약품)
- drug_name: 약품명
- ingredient: 성분명
- efficacy: 효능
- dosage: 용량
- precautions: 주의사항
- company: 회사명

### Post (게시글)
- title: 제목
- content: 내용
- author: 작성자 (User FK)
- views: 조회수

### Profile (사용자 프로필)
- user: 사용자 (User OneToOne)
- phone: 전화번호
- bio: 소개

## MySQL 설정 (선택사항)

`settings.py`에서 데이터베이스 설정 변경:

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

## 라이선스

MIT License

## 기여

이슈와 풀 리퀘스트를 환영합니다.

## 주의사항

- 본 시스템의 의약품 정보는 참고용이며, 실제 의료 진단이나 치료를 대신할 수 없습니다.
- 의약품 사용은 반드시 전문가(의사, 약사)의 지시에 따라야 합니다.
