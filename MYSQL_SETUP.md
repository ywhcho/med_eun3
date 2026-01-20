# MySQL 설정 가이드

이 문서는 med_eun3 프로젝트를 MySQL 데이터베이스와 함께 사용하는 방법을 설명합니다.

## 1. MySQL 서버 설치 및 설정

### MySQL 설치
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install mysql-server

# macOS (Homebrew)
brew install mysql

# Windows
# MySQL 공식 웹사이트에서 설치 프로그램 다운로드
# https://dev.mysql.com/downloads/mysql/
```

### MySQL 서비스 시작
```bash
# Ubuntu/Debian
sudo service mysql start

# macOS
brew services start mysql

# Windows
# 서비스 앱에서 MySQL 서비스 시작
```

## 2. 데이터베이스 생성

MySQL에 로그인:
```bash
mysql -u root -p
```

데이터베이스 생성:
```sql
CREATE DATABASE med_eun3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

사용자 생성 및 권한 부여:
```sql
CREATE USER 'med_eun3_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON med_eun3.* TO 'med_eun3_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## 3. Django 설정 변경

`med_eun3_project/settings.py` 파일을 열고 DATABASES 설정을 수정:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'med_eun3',
        'USER': 'med_eun3_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

## 4. mysqlclient 설치 확인

```bash
pip install mysqlclient
```

만약 설치 중 오류가 발생하면:

### Ubuntu/Debian
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```

### macOS
```bash
brew install mysql-client
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
pip install mysqlclient
```

### Windows
```bash
# Visual C++ Build Tools 설치 필요
# https://visualstudio.microsoft.com/downloads/
pip install mysqlclient
```

## 5. 마이그레이션 실행

```bash
# 마이그레이션 파일 생성 (이미 있으면 생략)
python manage.py makemigrations

# 데이터베이스에 적용
python manage.py migrate
```

## 6. 샘플 데이터 생성

```bash
python manage.py create_sample_medicines
```

## 7. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

## 8. 서버 실행

```bash
python manage.py runserver
```

## MySQL 접속 확인

다음 명령어로 데이터가 제대로 들어갔는지 확인:

```bash
mysql -u med_eun3_user -p med_eun3
```

```sql
-- 테이블 확인
SHOW TABLES;

-- 의약품 데이터 확인
SELECT * FROM medicine_medicine;

-- 사용자 확인
SELECT * FROM auth_user;
```

## 문제 해결

### 연결 오류
```
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server...")
```
- MySQL 서버가 실행 중인지 확인
- HOST와 PORT 설정 확인
- 방화벽 설정 확인

### 권한 오류
```
django.db.utils.OperationalError: (1045, "Access denied for user...")
```
- 사용자 이름과 비밀번호 확인
- MySQL에서 사용자 권한 재확인

### 문자 인코딩 오류
- 데이터베이스 생성 시 utf8mb4 사용
- settings.py의 OPTIONS에 charset 설정 확인

## 백업 및 복원

### 백업
```bash
mysqldump -u med_eun3_user -p med_eun3 > backup.sql
```

### 복원
```bash
mysql -u med_eun3_user -p med_eun3 < backup.sql
```

## 보안 권장사항

1. **강력한 비밀번호 사용**: 데이터베이스 사용자 비밀번호를 복잡하게 설정
2. **환경 변수 사용**: settings.py에 비밀번호를 직접 입력하지 말고 환경 변수 사용
   ```python
   import os
   'PASSWORD': os.environ.get('DB_PASSWORD', 'default_password'),
   ```
3. **localhost 제한**: 원격 접속이 필요하지 않다면 localhost로 제한
4. **정기 백업**: 중요한 데이터는 정기적으로 백업

## 추가 정보

- MySQL 공식 문서: https://dev.mysql.com/doc/
- Django MySQL Notes: https://docs.djangoproject.com/en/stable/ref/databases/#mysql-notes
- mysqlclient 문서: https://github.com/PyMySQL/mysqlclient
