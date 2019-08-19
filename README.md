### Many Example for usefull Django Framework
------------------------------------------------------------------------------------------------
## Versioning requirements
  - Python 3.6
  - Django 2.2.1
  - SqlLite 3
  - DRF(djangorestframework) 3.10
  - doker 18.09.8
  - docker-compose 1.24.1
  - flake8

### How to Run this repository on your machine :
  - This Project is already using Docker container to manage the instalation file.
  - Cek the Requirements.txt file on root of project before you clone this repository.
  - If you already installed docker or docker compose, run with docker-compose up.
  - If you dont have docker or docker-compose, please run requirements.txt manualy.

-------------------------------------------------------------------------------------------------


### Samples Update Almost Daily :

* [Custom Users Model Before Migrations](https://github.com/Ekhel/django-practical/tree/master/practical/core)
* [Sampel TDD / Test Development Driven](https://github.com/Ekhel/django-practical/blob/master/practical/practical/tests.py)
* [Use Template in our Project](https://github.com/Ekhel/django-practical/tree/master/practical/core)
  - make folder static in our app copas file css, js, from template you are using
  - go to the settings file in the root of project, make sure your settings have this (STATIC_URL = '/static/')
* [REST User Authentication API With DRF(Django Rest Framework) And Token Serializers](https://github.com/Ekhel/django-practical/tree/master/practical/authapi)
* [Implement GraphQL Schema using graphene django](https://github.com/Ekhel/django-practical/tree/master/practical/editor)
  - Make sure you have 2 Level schema in your project root and apps
  - this sample don't have config in file settings.py couse i have pass into ursl.py (root project)