# Animal Rescue and Shelter
Capstone project of the Full Stack Nanodegree Program.

## What Will I Build 
A full stack website for an animal and rescue shelter on a specific city that encorges its users to adopt rescued pets.

## Getting Started
You can follow instructions specified in:
1. [`./backend/README.md`](./backend/README.md)
2. [`./frontend/README.md`](./frontend/README.md)

## API Endpoints
The following endpoints are implemented and they perform [CRUD](https://www.codecademy.com/articles/what-is-crud) operations on the [PostgresSQL](https://www.postgresql.org/about/) database:

All CREATE Requests:
* `POST '/interview'`
* `POST '/pet'`
### Request: ```POST '/interview'```
#### Body -
```
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
### Request: ```POST '/pet'```
#### Body -
```
{
    
}
```
### Response: Status Code - 201 (CREATED)
```

```
All READ Requests:
* `GET '/all-pets'`
* `GET '/interviews'`
* `GET '/pets-detail'`
* `GET '/all-adopted-pets'`
* `GET '/all-Interviews'`

### Request:
```GET '/all-pets'```
### Response:
Status Code - 200 (OK)
#### Body -
```
{

}
```

UPDATE
* ``
```

```
DELETE
* ``
```

```