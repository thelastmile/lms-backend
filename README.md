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

=======
###Jenkins setup - AWS Elastic Beanstalk
Access http://52.35.21.48:8080/job/TLM%20LMS%20Backend/ for the Jenkins configuration used for automating dev updates when the master branch is updated and pushed to github.

####The additional information for how to setup Jenkins for a new backend deployment to Elastic Beanstalk job is below

* Create the new job in Jenkins that pulls code from https://github.com/thelastmile/lms-backend git repo based on an event trigger setup on github.  Use the above linked Jenkins job as a model.
  * Use the following Command under the 'Build Process' section -> Execute Shell
  ```
  cd lms-backend
  eb use <YOUR ELASTIC BEANSTALK ENVIRONMENT NAME>"
  eb deploy --profile tlm
  ```
  * Save your Jenkins job.
  * RUN the Jenkins job.  It will fail on the `eb use` command but it will setup your filesystem for the next steps.

* Ensure that the build is properly extracting the files from the master branch to the local build directory
  * ssh onto Jenkins machine and `cd /var/lib/jenkins/workspace/PATHTOPROJECT/lms-backend`
  * `ls -a` to see that all files are there as expected, including the .elasticbeanstalk and .ebextensions directory.  If so then proceed with next step.
* install the eb tool (Requires Python 2.7 installed on Jenkins machine)
  * `pip install awsebcli`
  * verify it works `eb --version` should print something like "EB CLI 3.2.2 (Python 2.7.9)"
  * For more details on installing python 2.7, pip and the aws cli that includes eb go here: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html
 * Configure your access
  * double check your security/creds `vi /var/lib/jenkins/.aws/credentials` and add a new entry if needed.  We're using "tlm" for this example.  These keys and IDs are created in the AWS console admin tool.  If your OPS/Jenkins machine will have several accounts for multiple clients this will be mandatory, if not you could keep the TLM key as the 'default'.
   * Will look like this
   ```
   [default]
   aws_access_key_id = <THEKEYID>
   aws_secret_access_key = <THEACCESKEY>

   [clientb]
   aws_access_key_id = <THEKEYID>
   aws_secret_access_key = <THEACCESKEY>

   [tlm]
   aws_access_key_id = <THEKEYID>
   aws_secret_access_key = <THEACCESKEY>
   ```
  * Follow directions here http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html for configuring your user access to the new Elastic Beanstalk environment.  The link also provides information pertaining to how to create the new Elastic Beanstalk environemnt if you havent' created one yet.  It can be done via the CLI or via the web management console.  During configuration:
   * The environment must be python 2.7
   * A postgres database must be added
 * The environment and required packages have all already been setup and can be seen in the `.ebextensions` directory
 * Edit the `.elasticbeanstalk/config.yml` to fit your environment for production.  Commit this file to git/github after changed!  The production path to the project and environment should remain in this file at all times.
* test your first deployment specifiying the profile to use `eb deploy --profile tlm`
* Once deployment is successful from command prompt then exit from ssh and you should now be able to successfully run manual builds from the UI and git-triggered builds to elastic beanstalk automagically. :)
* To confirm correct operation, visit the app /admin like: http://tlm-lms-backend.elasticbeanstalk.com/admin/ and you should see the admin login area.  The initial login on deployment is set to admin/admin.
* Login and change the admin password immediately and create a new user for yourself, marked as admin aswell.

### CENTOS7
```
git clone https://github.com/thelastmile/lms-backend.git
cd lms-backend/lmsbackend
yum install libjpeg-turbo-devel
```

Update config for postgres
`cp local_settings.example.py local_settings.py`

add this to local settings:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lms',
        'USER': 'lmsuser',
        'PASSWORD': '@ech043v3r@lms@',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
run
```
yum install python-virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py syncdb
pip install gunicorn
gunicorn lmsbackend.wsgi -w 4 --bind 0.0.0.0:8000
```

### API Live Docs
Swagger interactive docs can be seen at ANY deployment backend paths by adding "/api/docs/" to the server path.
For example: http://tlmlmsbackend-staging.us-west-2.elasticbeanstalk.com/api/docs/

Or a future example on location:
http://ironwood-lms-backend/api/docs/

To view the docs you must be an authenticated Super User.  Ensure that you've logged in at /admin before trying to visit /api/docs/
