# lms-backend


###Installation
```
git clone git@github.com:thelastmile/lms-backend.git
cd lms-backend
```

###Setup Virtual Environment
```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

###Initial Setup

```
python manage.py syncdb --noinput
python manage.py migrate
./manage.py loaddata initial_data__groups
python manage.py createsuperuser // enter in credentials you would like to log in
```
`cp local_settings.example.py local_settings.py` <- edit your local_settings.py to meet your needs

###Run the server (local dev)
`./manage.py runserver`

Open your browser to `http://127.0.0.1:8000/admin/`

Enter your user credentials that were created

* Create a separate user that will belong to each group for full testing spectrum
