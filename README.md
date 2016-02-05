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

###Jenkins setup - AWS Elastic Beanstalk
Access http://52.35.21.48:8080/job/TLM%20LMS%20Backend/ for the Jenkins configuration used for automating dev updates when the master branch is updated and pushed to github.

The additional information for how to setup Jenkins for a new job is below:

* Create the new job in Jenkins that pulls code from https://github.com/thelastmile/lms-backend git repo based on an event trigger setup on github.  Use the above linked Jenkins job as a model.
  * Use the following Command under the 'Build Process' section -> Execute Shell

tlm-lms-backend is the current environment_name for dev.  In the code below replace tlm-lms-backend with the environment_name as it is setup on AWS Elastic Beanstalk

```
cd lms-backend
eb use tlm-lms-backend
eb deploy
```

* Ensure that the build is properly extracting the files from the master branch to the local build directory
  * ssh onto Jenkins machine and `cd /var/lib/jenkins/workspace/PATHTOPROJECT/`
  * `ls -a` to see that all files are there as expected, including the venv directory.  If so then proceed with next step.
* install the eb tool (Requires Python 2.7 installed on Jenkins machine)
  * `pip install awsebcli`
  * verify it works `eb --version` should print something like "EB CLI 3.2.2 (Python 2.7.9)"
  * For more details on installing python 2.7, pip and the aws cli that includes eb go here: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html

