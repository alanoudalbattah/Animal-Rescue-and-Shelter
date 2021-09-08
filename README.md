# Animal Rescue and Shelter - Capstone Project
This project is the Capstone project for the `Udacity Full-Stack Developer Nanodegree` Program.

Concepts and the skills summrized by udacity: 
* Coding in Python 3
* Relational Database Architecture
* Modeling Data Objects with SQLAlchemy
* Internet Protocols and Communication
* Developing a Flask API
* Authentication and Access
* Authentication with Auth0
* Authentication in Flask
* Role-Based Access Control (RBAC)
* Testing Flask Applications
* Deploying Applications


[Application Heroku Link](http)

## Content
1. [Overview](#Overview)
1. [Tech Stack](#Tech-Stack)
1. [Getting Started](#Getting-Started)
1. [API Documentation](#API-Docs)
1. [Authentication](#Authentication)
1. [Heroku Deployment](#Deployment)
1. [Frontend](#frontend)

<a name="Overview"></a>

## Overview
Animal Rescue and Shelter enables its users to look for the perfect friend (a cat or a dog to adopt) for the perfect home (users of the website). It eases the process of booking an interview with the shelter and searching for a pet to adopt. And its encorges its users to adopt rescued pets.

The shelter website is designed to cover one city and all process after the interview is not included in the scope of this project.

<a name="Tech-Stack"></a>

## Tech Stack (Dependencies)
----
- Python environments tool: [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- ORM library: [SQLAlchemy](https://www.sqlalchemy.org/)
- Database: [PostgresSQL](https://www.postgresql.org/)
- Server language and server framework: [Python3](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) and [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Creating and running schema migrations: [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 




<a name="Getting-Started"></a>

## Getting Started
----
To work with the application locally first make sure you have [python](https://www.python.org/downloads/) installed.

Then:

1. Clone the Repository

2. Set up a virtual environment using [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. Install pip Dependencies:
```Shell
pip install -r requirements.txt
```
4. Run Database [Migrations](https://flask-migrate.readthedocs.io/en/latest/)
5. Run the Flask Application locally:
```Shell
export FLASK_APP=myapp
export FLASK_ENV=development 
flask run

```
6. Verify on the Browser
Navigate to project homepage http://127.0.0.1:5000/ or http://localhost:5000

7. Run unittests
```Shell
python unittest_app.py
```


<a name="API-Docs"></a>

## API Documentation
----
You can view the documentation at [API Documentation](./API_DOCS.md)

<a name="Authentication"></a>

## Authentication
----
Protected API Endpoints are decorated with Auth0 permissions. to use the project locally, you need to config Auth0 accordingly. read[Authentication with Auth0](./auth/README.md) for more details.

<a name="Deployment"></a>

## Heroku Deployment
----
This project is deployed to Heroku at the following link: https://animal-rescue-and-shelter.herokuapp.com/

<a name="Frontend"></a>

## Frontend
----
For now only the home page has been devoloped.

