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
2. [Tech Stack](#Tech-Stack)
3. [Project Structure](#Project-Structure)
4. [Getting Started](#Getting-Started)
5. [API Endpoints](#API-Endpoints)


## Overview
Animal Rescue and Shelter enables its users to look for the perfect friend (a cat or a dog to adopt) for the perfect home (users of the website). It eases the process of booking an interview with the shelter and searching for a pet to adopt. And its encorges its users to adopt rescued pets.

The shelter website is designed to cover one city and all process after the interview is not included in the scope of this project.

<a name="Tech-Stack"></a>

## Tech Stack (Dependencies)
- Python environments tool: [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- ORM library: [SQLAlchemy](https://www.sqlalchemy.org/)
- Database: [PostgresSQL](https://www.postgresql.org/)
- Server language and server framework: [Python3](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) and [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Creating and running schema migrations: [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 


<a name="Project-Structure"></a>

## Project Structure
```

```

<a name="Getting-Started"></a>

## Getting Started
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


<a name="API-Endpoints"></a>

## API Endpoints
### Endpoints `/` `/about`
#### Behaviour: These endpoints don't perform any [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the database they just return a rendered file.
#### Response: Status Code - 200 (OK)

### Endpoints [`/interview`](#post-interview) [`/pet`](#post-pet) `` `` `` `` `` ``
#### Behaviour: These endpoints perform [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the [PostgresSQL](https://www.postgresql.org/about/) database.

CREATE Requests:
* [`POST '/interview'`](#post-interview)
* [`POST '/pet'`](#post-pet)

READ Requests:
* [`GET '/all-pets'`](#)
* [`GET '/interviews'`](#)
* [`GET '/pets-detail'`](#)
* [`GET '/all-adopted-pets'`](#)
* [`GET '/all-Interviews'`](#)

UPDATE Requests:
* [`PATCH '/'`](#)
* [`PATCH '/'`](#)
* [`PATCH '/'`](#)
* [`PATCH '/'`](#)

DELETE Requests:
* [`DELETE '/'`](#)
* [`DELETE '/'`](#)
* [`DELETE '/'`](#)
* [`DELETE '/'`](#)


<a name="post-interview"></a>

### 1. POST ```/interview```
Creates a new interview.

#### Request Body -
```JSON
{
    "specie_id": 1,
    "breed_id": 1,
    "name": "Hamoosh",
    "image_link": "image_link",
    "age_in_months": 120,
    "gender": "Male",
    "vaccinated": true,
    "letter_box_trained": true,
    "note": "Likes to play with lazerz :)"
}
```
#### Response: Status Code - 201 (CREATED)

<a name="post-pet"></a>

### 2. POST /pet
Creates a new pet.

#### Request: ```POST '/pet'```
#### Body -
```JSON
{
    
}
```
#### Response: Status Code - 201 (CREATED)

### Error Handlers for: `400` `401` `403` `404` `422` `500`
All error handlers return a JSON object with the request status and error message i.e.:
```JSON
{
   "success":false,
   "error":400,
   "message":"constraint violation, could not be deleted."
}
```