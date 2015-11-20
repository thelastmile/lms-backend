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

###Local Development Server
```
python manage.py syncdb --noinput
python manage.py migrate
python manage.py createsuperuser // enter in credentials you would like to log in
./manage.py runserver
```

Open your browser to ```http://127.0.0.1:8000/admin/```

Enter your user credentials that were created

###Initial Data Setup

Create the following Groups via Django Admin:

`Inmate`, `Facilitator`, `Super Admin`

Create a separate user that will belong to each group for full testing spectrum
