Angryjobs
=========

Web site developed with Django that shows quite interesting job offers from a well known job engine in Spain

Steps to perform before running the server
==========================================

You need to set these environment variables:

**TE_GLOBAL_PWD:**
Password used when an account is created for an user from Twitter

**TE_CONSUMER_KEY:**
You need to create a Twitter application to allow users to login into the application. This is the consumer key of that application.

**TE_CONSUMER_SECRET:**
You need to create a Twitter application to allow users to login into the application. This is the consumer secret of that application.

**TE_API_USER:**
The user in which name the API inserts data into the application. It can be created here: http://127.0.0.1:8000/admin

**TE_API_KEY:**
The key for the user who has the right to insert data using the API. It can be created here: http://127.0.0.1:8000/admin

**TE_CAPTCHA_PUBLIC_KEY:**
Public key for captcha. You can get one from http://www.google.com/recaptcha

**TE_CAPTCHA_PRIVATE_KEY:**
Private key for captcha service. You can get one from http://www.google.com/recaptcha

If you are in Mac or are using bash, you can do the following:

    export TE_GLOBAL_PWD=y34h
    export TE_CONSUMER_KEY=y34h
    export TE_CONSUMER_SECRET=y34h
    export TE_API_USER=y34h
    export TE_API_KEY=y34h
    export TE_CAPTCHA_PUBLIC_KEY=y34h
    export TE_CAPTCHA_PRIVATE_KEY=y34h

Once you have done the above steps, ypou can follow with the folllowing point.

Steps to run the server
=======================

Setup the environment

    1.  chmod +x setup_env.sh
    2.  ./setup_env.sh
    3.  source __venv__/bin/activate

Install dependencies

    4.  pip install -r requirements/local.txt

Run server

    5.  django-admin.py syncdb --pythonpath='angryjobs' --settings=angryjobs.settings.local
    6.  django-admin.py runserver --pythonpath='angryjobs' --settings=angryjobs.settings.local

Fetch data and save into app

    7.  python updater/fetch_data.py
