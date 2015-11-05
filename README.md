# lms-backend


###Installation
1. ```git clone git@github.com:thelastmile/lms-backend.git```
2. ```cd lms-backend```

###Setup Virtual Environment
```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

###Local Development Server
```
python manage.py syncdb --noinput
python manage.py migrate
python manage.py createsuperuser
./manage.py runserver
```

Open your browser to ```http://127.0.0.1:8000/```
