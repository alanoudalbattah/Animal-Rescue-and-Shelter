
# API Endpoints
## Overview
Here you can find the full documentation of the API Endpoints for Animal Rescue and Shelter.
## Content
1. [Endpoints](#Endpoints)
1. [Error Handlers](#Error-Handlers)

<a name="Endpoints"></a>

## Endpoint `/`
#### Behaviour: This endpoint don't perform any [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the database it just return a rendered template.
#### Response: Status Code - 200 (OK)


## Endpoints
CREATE Requests:
1.  [`POST /specie`](#post-specie)
1.  [`POST /breed`](#post-breed)
1.  [`POST /pet`](#post-pet)
1.  [`POST /user`](#post-user)
1.  [`POST /interview`](#post-interview)


READ Requests:
1. [`GET /all-species`](#get-all-species)
1. [`GET /specie/<int:_id>`](#get-specie-byid)
1. [`GET /all-breeds`](#get-all-breeds)
1. [`GET /breed/<int:_id>`](#get-breed-byid)
1. [`GET '/all-pets'`](#get-all-pets)
1. [`GET '/pet/<int:_id>'`](#get-pet-byid)
1. [`GET '/all-interviews'`](#get-all-interviews)
1. [`GET '/interview/<int:_id>'`](#get-interview-byid)
1. [`GET '/interviews/<int:_id>'`](#get-interviews-byid)

UPDATE Requests:
1. [`PATCH /specie/<int:_id>`](#pat-specie-byid)
1. [`PATCH /breed/<int:_id>`](#pat-breed-byid)
1. [`PATCH /pet/<int:_id>`](#pat-pet-byid)
1. [`PATCH /interview/<int:_id>`](#pat-interview-byid)

DELETE Requests:
1. [`DELETE /specie/<int:_id>`](#del-specie-byid)
1. [`DELETE /breed/<int:_id>`](#del-breed-byid)
1. [`DELETE /pet/<int:_id>`](#del-pet-byid)
1. [`DELETE /interview/<int:_id>`](#del-interview-byid)

#### Behaviour: These endpoints perform [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the [PostgresSQL](https://www.postgresql.org/about/) database.


<a name="post-specie"></a>

# POST
## 1. `POST` ```/specie```

Creates a new specie i.e. a Cat.

#### Request Body -
```JSON
{
    "specie": "Cat"
}
```
#### Response: Status Code - 201 (CREATED)
```JSON
{
    "newSpecie": {
        "id": 1,
        "name": "Cat"
    }
}
```

<a name="post-breed"></a>

## 2. `POST` ```/breed```

Creates a new breed e.g. Rag Doll.

#### Request Body -
```JSON
{
    "specie": "Cat",
    "breed": "Rag Doll"
}
```
#### Response: Status Code - 201 (CREATED)
```JSON
{
    "newBreed": {
        "id": 1,
        "image": null,
        "name": "Rag Doll",
        "specie_id": 1
    }
}
```


<a name="post-pet"></a>

## 3. `POST` ```/pet```
Creates a new Pet post.

#### Request Body -
```JSON
{
    "breed": "Rag Doll",
    "name": "Kitkat",
    "image_link": "https://someImageURL.com",
    "age_in_months": 200,
    "gender": "female",
    "vaccinated": true,
    "letter_box_trained": true,
    "note": "Likes to play with lazerz"
}
```
#### Response: Status Code - 201 (CREATED)
```JSON
{
    "details": {
        "age_in_months": 200,
        "breed_id": 1,
        "breed_name": "Rag Doll",
        "gender": "female",
        "id": 1,
        "image_link": "https://someImageURL.com",
        "letter_box_trained": true,
        "name": "Kitkat",
        "note": "Likes to play with lazerz",
        "vaccinated": true
    }
}
```

<a name="post-pet"></a>

## 3. `POST` ```/user```
Creates a new user.

#### Request Body -
```JSON
  {
      "first_name":"alanoud",
      "last_name":"albattah",
      "email":"alanoudalbattah@outlook.com",
      "mobile": "054211111",
      "age": 23
  }
```
#### Response: Status Code - 201 (CREATED)
```JSON

{
    "details": {
        "age": "23",
        "email": "alanoudalbattah@outlook.com",
        "id": 1,
        "mobile": "054211111",
        "name": "alanoud albattah"
    }
}

```
<a name="post-interview"></a>

## 4. `POST` ```/interview```

Creates a new interview.

#### Request Body -
```JSON
{
    "pet_id": 1,
    "user_id": 1,
    "year": 2021,
    "month": 2,
    "day": 2,
    "hour": 1,
    "minute": 0
}
```
#### Response: Status Code - 201 (CREATED)
```JSON
{
    "new_interview": {
        "date": "02/02/2021",
        "id": 1,
        "interview for": "Kitkat",
        "interview with": "alanoud albattah",
        "pet_id": 1,
        "time": "01:00",
        "user_id": 1
    }
}

```
# GET
<a name="get-all-species"></a>

## 1. `GET` ```/all-species```

Views all species i.e. Cat and Dog

#### Response: Status Code - 200 (OK)
```JSON
{
  "all species": [
    {
      "id": 1, 
      "name": "Cat"
    }, 
    {
      "id": 2, 
      "name": "Dog"
    }
  ]
}
```

<a name="get-specie-byid"></a>

## 2. `GET` ```/specie/<int:_id>```

Views a specific specie by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
  "specie details": {
    "id": 1, 
    "name": "Cat"
  }
}
```

<a name="get-all-breeds"></a>

## 3. `GET` ```/all-breeds?page=${integer}```

Views all on a paginated set of breeds by given page. 

#### Response: Status Code - 200 (OK)
#### and an object with 10 paginated breeds
```JSON
{
    "all breeds": [
        {
            "id": 1,
            "image": "https://some_image_link.com/",
            "name": "Rag Doll",
            "specie_id": 1
        },
        {
            "id": 2,
            "image": "https://some_image_link.com/",
            "name": "LaPerm",
            "specie_id": 1
        },
        {
            "id": 3,
            "image": "https://some_image_link.com/",
            "name": "Himalayan",
            "specie_id": 1
        },
        {
            "id": 4,
            "image": "https://some_image_link.com/",
            "name": "Havana Brown",
            "specie_id": 1
        },
        {
            "id": 5, 
            "image": "https://some_image_link.com/", 
            "name": "Bombay", 
            "specie_id": 1
        }
    ]
}
```

<a name="get-breed-byid"></a>

## 4. `GET` ```/breed/<int:_id>```

Views a specific breed by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
  "breed details": {
    "id": 1, 
    "image": "https://some_image_link.com/", 
    "name": "Rag Doll", 
    "specie_id": 1
  }
}
```

<a name="get-all-pets"></a>

## 5. `GET` ```/all-pets```

Views all pets posts.

#### Response: Status Code - 200 (OK)
```JSON
{
    "pets": [
        {
            "age_in_months": 200,
            "breed_id": 1,
            "breed_name": "Rag Doll",
            "gender": "female",
            "id": 2,
            "image_link": "https://someImageURL.com",
            "letter_box_trained": true,
            "name": "Kitkat",
            "note": "Likes to play with lazerz",
            "vaccinated": true
        },
        {
            "age_in_months": 200,
            "breed_id": 2,
            "breed_name": "LaPerm",
            "gender": "male",
            "id": 3,
            "image_link": "https://someImageURL.com",
            "letter_box_trained": true,
            "name": "Twix",
            "note": null,
            "vaccinated": true
        },
        {
            "age_in_months": 300,
            "breed_id": 3,
            "breed_name": "Himalayan",
            "gender": "male",
            "id": 4,
            "image_link": "https://someImageURL.com",
            "letter_box_trained": true,
            "name": "Bompa",
            "note": null,
            "vaccinated": true
        }
    ]
}
```


<a name="get-pet-byid"></a>

## 6. `GET` ```/pet/<int:_id>```

Views a specific pet by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "pet": {
        "age_in_months": 200,
        "breed_id": 2,
        "breed_name": "LaPerm",
        "gender": "female",
        "id": 3,
        "image_link": "https://someImageURL.com",
        "letter_box_trained": true,
        "name": "Twix",
        "note": null,
        "vaccinated": true
    }
}
```
<a name="get-all-interviews"></a>

## 7. `GET` ```/all-interviews```

Views all interviews previous and upcoming.

#### Response: Status Code - 200 (OK)
```JSON
{
    "all interviews": [
        {
            "date": "02/09/2021",
            "id": 2,
            "interview for": "Kitkat",
            "interview with": "alanoud albattah",
            "pet_id": 2,
            "time": "01:00",
            "user_id": 1
        },
        {
            "date": "02/25/2021",
            "id": 3,
            "interview for": "Twix",
            "interview with": "Ahmed AlSomthing",
            "pet_id": 3,
            "time": "05:00",
            "user_id": 2
        }
    ]
}
```
<a name="get-interview-byid"></a>

## 8. `GET` ```/interview/<int:_id>```

Views a specific interview by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "interview details": {
        "date": "02/25/2021",
        "id": 3,
        "interview for": "Twix",
        "interview with": "Ahmed AlSomthing",
        "pet_id": 3,
        "time": "05:00",
        "user_id": 2
    }
}
```
<a name="get-interviews-byid"></a>

## 9. `GET` ```/interviews/<int:_id>```

Views all interviews for a specific user specified by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "interviews": [
        2,
        3
    ]
}
```


# PATCH
<a name="pat-specie-byid"></a>

## 1. `PATCH` ```/specie/<int:_id>```

Updates a specific specie by id received from the params.

#### Request Body -
```JSON
{
    "name":"Dog"
}
```
#### Response: Status Code - 200 (OK)
```JSON
{
    "specie": {
        "id": 1,
        "name": "Dog"
    }
}
```


<a name="pat-breed-byid"></a>

## 2. `PATCH` ```/breed/<int:_id>```

Updates a specific breed by id received from the params.

#### Request Body -
```JSON
{
    "specie_id":"2"
}
```
#### Response: Status Code - 200 (OK)
```JSON
{
    "breed": {
        "id": 1,
        "image": "https://some_image_link.com/", 
        "name": "Rag Doll", 
        "specie_id": 2
    }
}
```

<a name="pat-pet-byid"></a>

## 3. `PATCH` ```/pet/<int:_id>```

Updates a specific pet by id received from the params.

#### Request Body -
```JSON
{
    "breed": "Rag Doll"
}
```
#### Response: Status Code - 200 (OK)
```JSON
{
    "pet": {
        "age_in_months": 200,
        "breed_id": 1,
        "breed_name": "Rag Doll",
        "gender": "female",
        "id": 2,
        "image_link": "https://someImageURL.com",
        "letter_box_trained": true,
        "name": "Kitkat",
        "note": "Likes to play with lazerz",
        "vaccinated": true
    }
}
```

<a name="pat-interview-byid"></a>

## 4. `PATCH` ```/interview/<int:_id>```

Updates a specific interview by id received from the params.

#### Request Body -
```JSON
{
    "year": 2021,
    "day": 9
}
```
#### Response: Status Code - 200 (OK)
```JSON
{
    "interview updated": {
        "date": "02/09/2021",
        "id": 2,
        "interview for": "Kitkat",
        "interview with": "alanoud albattah",
        "pet_id": 2,
        "time": "01:00",
        "user_id": 1
    }
}
```

# DELETE
<a name="del-specie-byid"></a>

## 1. `DELETE` ```/specie/<int:_id>```

Deletes a specific specie by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "specie_id": 1
}
```


<a name="del-breed-byid"></a>

## 2. `DELETE` ```/breed/<int:_id>```

Deletes a specific breed by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "breed_id": 1
}
```

<a name="del-pet-byid"></a>

## 3. `DELETE` ```/pet/<int:_id>```

Deletes a specific pet by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "pet_id": 1
}
```


<a name="del-interview-byid"></a>

## 4. `DELETE` ```/interview/<int:_id>```

Deletes a specific interview by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "interview_id": 1
}
```


<a name="Error-Handlers"></a>

# Error Handlers
Error handlers are avalible for: `400` `401` `403` `404` `422` `500`

All error handlers return a JSON object with the request status and error message e.g.:
```JSON
{
   "success":false,
   "error":400,
   "message":"constraint violation, could not be deleted."
}
```
