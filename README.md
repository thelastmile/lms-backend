# lms-backend

###Prerequisites

* python 2.7
* postgres installed locally

###Installation
```
git clone git@github.com:thelastmile/lms-backend.git
cd lms-backend
```

###Setup Virtual Environment For DEV
```
virtualenv venv
. venv/bin/activate
pip install -r requirements-dev.txt
```

###Setup Virtual Environment For PROD
```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

###Initial Setup

```
cp local_settings.example.py local_settings.py
python manage.py syncdb --noinput
python manage.py migrate
./manage.py loaddata initial_data
python manage.py createsuperuser
```



Edit your local_settings.py to meet your needs.  For local dev the as-is local_settings.example.py is good to go.  For production Debug must be off, S3 keys must be added and STATICFILES_STORAGE/DEFAULT_FILE_STORAGE lines removed.

You may want to set your dev local settings as follows to allow the MEDIA path to live in the root of your project (it won't be committed to git)
```
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = '%s/media/' % SETTINGS_PATH
```

###Run the server (local dev)
`./manage.py runserver`

Open your browser to `http://127.0.0.1:8000/admin/`

Enter your user credentials that were created

Add the group `Super Admin` to your admin user

Create a separate user that will belong to each group for full testing spectrum

###Getting the latest updates
```
cd <appdir>
. venv/bin/activate
git checkout master
git pull
python manage.py syncdb --noinput
python manage.py migrate
./manage.py loaddata initial_data
```

###Jenkins

####On Jenkins host

Install and configure AWS cli tool with keys for access

