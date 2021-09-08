
# API Endpoints
## Overview
Here you can find the full documentation of the API Endpoints for Animal Rescue and Shelter.
## Content
1. [Error Handlers](#Error-Handlers)
1. [Endpoints](#Endpoints)

<a name="Error-Handlers"></a>

## Error Handlers
Error handlers are avalible for: `400` `401` `403` `404` `422` `500`

All error handlers return a JSON object with the request status and error message e.g.:
```JSON
{
   "success":false,
   "error":400,
   "message":"constraint violation, could not be deleted."
}
```

<a name="Endpoints"></a>

## Endpoints 
`/` `/about`
#### Behaviour: These endpoints don't perform any [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the database they just return a rendered file.
#### Response: Status Code - 200 (OK)

[`/interview`](#post-interview) [`/pet`](#post-pet) `` `` `` `` `` ``
#### Behaviour: These endpoints perform [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the [PostgresSQL](https://www.postgresql.org/about/) database.

CREATE Requests:
1.  [`POST /specie`](#post-specie)
1.  [`POST /breed`](#post-breed)

1.  [`POST /interview`](#post-interview)
1.  [`POST /pet`](#post-pet)

READ Requests:
1. [`GET /all-species`](#get-all-species)
1. [`GET /specie/<int:_id>`](#get-specie-byid)
1. [`GET /all-breeds`](#get-all-breeds)
1. [`GET /breed/<int:_id>`](#get-breed-byid)

1. [`GET '/all-pets'`](#)
1. [`GET '/interviews'`](#)
1. [`GET '/pets-detail'`](#)
1. [`GET '/all-adopted-pets'`](#)
1. [`GET '/all-Interviews'`](#)

UPDATE Requests:
1. [`PATCH /specie/<int:_id>`](#pat-specie-byid)
1. [`PATCH /breed/<int:_id>`](#pat-breed-byid)

1. [`PATCH '/'`](#)
1. [`PATCH '/'`](#)

DELETE Requests:
1. [`DELETE /specie/<int:_id>`](#del-specie-byid)
1. [`DELETE /breed/<int:_id>`](#del-breed-byid)

1. [`DELETE '/'`](#)
1. [`DELETE '/'`](#)

<a name="post-specie"></a>

### 1. `POST` ```/specie```

Creates a new specie i.e. a Cat.

#### Request Body -
```JSON
{
    "specie": "Cat"
}
```
#### Response: Status Code - 201 (CREATED)

<a name="post-breed"></a>

### 2. `POST` ```/breed```

Creates a new breed e.g. Rag Doll.

#### Request Body -
```JSON
{
    "specie": "Cat",
    "breed": "Rag Doll"
}
```
#### Response: Status Code - 201 (CREATED)

<a name="post-interview"></a>

### 3. `POST` ```/interview```

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

### 4. `POST` ```/pet```



<a name="get-all-species"></a>

### 1. `GET` ```/all-species```

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

### 2. `GET` ```/specie/<int:_id>```

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

### 3. `GET` ```/all-breeds```

Views all breeds.

#### Response: Status Code - 200 (OK)
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
      "name": "Bombay", 
      "specie_id": 1
    }
  ]
}
```

<a name="get-breed-byid"></a>

### 4. `GET` ```/breed/<int:_id>```

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
<a name="pat-specie-byid"></a>

### 1. `PATCH` ```/specie/<int:_id>```

Updates a specific specie by id received from the params.

#### Response: Status Code - 200 (OK)


<a name="pat-breed-byid"></a>

### 2. `PATCH` ```/breed/<int:_id>```

Updates a specific breed by id received from the params.

#### Response: Status Code - 200 (OK)


<a name="del-specie-byid"></a>

### 1. `DELETE` ```/specie/<int:_id>```

Deletes a specific specie by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "specie_id": 1
}
```


<a name="del-breed-byid"></a>

### 2. `DELETE` ```/breed/<int:_id>```

Deletes a specific breed by id received from the params.

#### Response: Status Code - 200 (OK)
```JSON
{
    "breed_id": 1
}
```