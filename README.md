# SSAFY Bigdata project

## :apple: How to Run 

### Sub1

```sh
cd sub1
pip install -r requirements.txt
python parse.py
python analyze.py
python visualize.py
```

- python parse.py 로 dump.pkl 를 만든다.

### Sub 2

**Backend**

```sh
cd sub2/backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

- python manage.py initialize 했을 때...
- [*] Loading data...
  [*] Initializing stores...
  [+] Done

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve
```



## :green_apple: 개발환경 세팅 

**Backend**

```
# 가상환경
python -m venv venv
Source venv/Scripts/activate
pip install -r requirements.txt
```

**추가설치**

```
# 회원가입,로그인,로그아웃
# pip install djangorestframework
pip install django-rest-auth
pip install django-cors-headers
# 소셜로그인 인증을 위한 등록
pip install django-allauth

pip freeze > requirements.txt
```

**backend/requirements.txt**

```shell
certifi==2020.6.20
chardet==3.0.4
defusedxml==0.6.0
Django==2.2.7
django-allauth==0.42.0
django-cors-headers==3.5.0
django-rest-auth==0.9.5
djangorestframework==3.10.3
idna==2.10
joblib==0.14.0
numpy==1.17.3
oauthlib==3.1.0
pandas==0.25.3
python-dateutil==2.8.1
python3-openid==3.2.0
pytz==2019.3
requests==2.24.0
requests-oauthlib==1.3.0
scikit-learn==0.21.3
scipy==1.3.1
six==1.15.0
sqlparse==0.3.0
urllib3==1.25.10
```
