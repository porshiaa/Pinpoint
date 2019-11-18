# PINPOINT PROJECT
Pinpoint Project:

Installation guide:
Clone repositry to local machine git clone https://github.com/aisd9561/ITECH

Create virtual environment using anaconda:

conda create -n pinpoint python=3.7.1

Activate virtual environment using:

conda activate pinpoint

In the working directory :

pip install -r requirements_personal.txt

Make Migrations:

python manage.py makemigrations 

Migrate Database:

python manage.py migrate

Populate the website:

python populate_pinpoint.py

Run the website using the local host:

python manage.py runserver
