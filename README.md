# Creating REST-API for CRUD microservice using flaskAPI.

## 1. Overview
What we'll be doing
1. Build REST API for Create, Read, Update and Delete User List from database
2. User will have email and name
3. Check duplicate from database before create or update user


## 2. Getting Started
git clone `https://github.com/rajanazirul/flask-CRUD.git`

`cd flask-CRUD`

Setup virtual environment

`virtualenv env`

for windows, copy path `\env\Scripts\activate.bat`

open terminal and paste the path. If success will show (env) at the terminal

install dependencies using pip

`pip install flask flask-sqlalchemy psycopg2 flask-migrate Flask-API autoenv Flask-Script pytest python-dotenv`

create .env file

for windows, .env contain:
```
FLASK_APP=run.py
APP_SETTINGS=development
DATABASE_URL=postgresql://user:password@localhost/crud_app
```

at terminal, while in virtual environment run following:
```
SET FLASK_APP=run.py
SET APP_SETTINGS=development
SET DATABASE_URL=postgresql://user:password@localhost/crud_app
```

for linux, .env contain:
```
export FLASK_APP="run.py"
export APP_SETTINGS="development"
export DATABASE_URL="postgresql://user:password@localhost/crud_app"
```

## 3. Setup Database using PostgreSQL
install pgadmin with postgresql on link `https://www.postgresql.org/download/`

add PATH `C/postgresql12/Bin` to windows environment

create user for postgresql

Start menu > All Programs > PostgreSQL 8.3 > psql to 'postgres'.

This opens up the psql interactive terminal.
`CREATE ROLE username LOGIN PASSWORD 'password' NOINHERIT CREATEDB;`

create database by using following command on psql
`createdb test_db`
`createdb crud_app`

migrate database by run
`python manage.py db init`
`python manage.py db migrate`
`python manage.py db upgrade`

open PGadmin to check database or use psql terminal by command `\c userlist`

## 3. Run app
`flask run --host=0.0.0.0 --port=80`

## 4. Test app 
open /instance/config.py
on TestingConfig, change username and password for test_db
on terminal run pytest
`pytest`

## 5. API guide
```
http://localhost/userlists/

http://localhost/userlists/<id>
```

Test using POSTMAN
```
POST/GET/PUT/DELETE  http://localhost/userlists/
GET/PUT/DELETE  http://localhost/userlists/<id>
```

example:
| KEY             | Value                   | 
| -------------   |-------------------------|
| name            | rajanazirul             | 
| email           | rajanazirul@gmail.com   |


Reference:
https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way#toc-time-to-test-
https://www.youtube.com/watch?v=eAPmXQ0dC7Q&t=3762s
https://support.esri.com/en/technical-article/000010234
