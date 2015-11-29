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
./manage.py loaddata initial_data__customcontenttypes
./manage.py loaddata initial_data__courses
python manage.py createsuperuser
cp local_settings.example.py local_settings.py
```



Edit your local_settings.py to meet your needs.  For local dev the as-is local_settings.example.py is good to go.  For production Debug must be off, S3 keys must be added and STATICFILES_STORAGE/DEFAULT_FILE_STORAGE lines removed.

You may want to set your dev local settings as follows to allow the MEDIA path to live in the root of your project (it won't be committed to git)
```STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = '%s/media/' % SETTINGS_PATH```

###Run the server (local dev)
`./manage.py runserver`

Open your browser to `http://127.0.0.1:8000/admin/`

Enter your user credentials that were created

Add the group `Super Admin` to your admin user

Create a separate user that will belong to each group for full testing spectrum

###Getting the latest updates
```
cd <appdir>
git checkout master
git pull
python manage.py syncdb --noinput
python manage.py migrate
./manage.py loaddata initial_data__groups
./manage.py loaddata initial_data__customcontenttypes
./manage.py loaddata initial_data__courses
```