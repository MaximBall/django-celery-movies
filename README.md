## General info
The project is intended to familiarize you with a certain technology stack, 
such as payment through Stripe, storing data in S3 Storage, etc..
	
## Technologies
Project is created with:
* Python: 3.8
* Django: 3.2
* AllAuth for authorization with Google
* Stripe - for PayMent
* AWS Amazon - S3 Storage for media, static files
* DB - sqlite3
	
## Setup
To run this project, install it locally:

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```