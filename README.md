# Animal Rescue and Shelter
``` This project is the Capstone project for my Udacity Full-Stack Developer Nanodegree Program. ```

Animal Rescue and Shelter enables its users to look for the perfect friend (a cat or a dog to adopt) for the perfect home (users of the website). It eases the process of booking an interview with the shelter and searching for a pet to adopt. And its encorges its users to adopt rescued pets.

The shelter website is designed to cover one city and all process after the interview is not included in the scope of this project.

[Application Heroku Link](http)

## Content
1. [Application Stack](#Application-Stack)
2. [Getting Started](#Getting-Started)
3. [API Endpoints](#API-Endpoints)


<a name="Application-Stack"></a>

## Application Stack

<a name="Getting-Started"></a>

## Getting Started
You can follow instructions specified in:
1. [`./backend/README.md`](./backend/README.md)
2. [`./frontend/README.md`](./frontend/README.md)

<a name="API-Endpoints"></a>

## API Endpoints
The API will return six (6) error types when a request fails: `400` `401` `403` `404` `422` `500`

All error handlers return a JSON object with the request status and error message i.e.:
```JSON
{
   "success":false,
   "error":400,
   "message":"constraint violation, could not be deleted."
}
```

Endpoints `/` `/about`

### Behaviour: 
These endpoints don't perform any [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the database they just return a rendered file

### Response: 
Status Code - 200 (OK)

See the endpoints frontend [here](./frontend/README.md)

Endpoints `POST '/interview'` `POST '/pet` `` `` `` `` `` ``

These endpoints perform [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the [PostgresSQL](https://www.postgresql.org/about/) database:

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

### 1. POST /interview
Creates a new interview.

#### Request: ```POST '/interview'```
#### Body -
```JSON
        {
          "specie_id"=1, 
          "breed_id"=1,

          "name" = Hamoosh
          "image_link" = image_link
          "age_in_months" = 120
          "gender" = Male
          "vaccinated" = true
          "letter_box_trained" = true
          "note" = "Likes to play with lazerz :)"

        }
```
### Response: Status Code - 201 (CREATED)

<a name="post-pet"></a>

### 2. POST /pet
Creates a new pet.

#### Request: ```POST '/pet'```
#### Body -
```JSON
{
    
}
```
### Response: Status Code - 201 (CREATED)