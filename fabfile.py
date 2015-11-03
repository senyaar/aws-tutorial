from fabric.api import run, local, hosts, cd
from fabric.contrib import django

django.project('viewcount')

def hello():
    print("Hello Fabric")

def local_deploy():
    local("./manage.py runserver")
