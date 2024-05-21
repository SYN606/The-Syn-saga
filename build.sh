#!/bin/bash

# prokject build

echo"Building the project"

python -m pip install -r requirements.txt

echo"stated making migrations"

python manage.py makemigrations --noinput
python manage.py migrate --noinput 

echo"migrate successfully"


