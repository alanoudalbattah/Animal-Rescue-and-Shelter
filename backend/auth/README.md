# Role-Based Access Control (RBAC)
Authentication and Authorization is implemented using [Auth0](https://auth0.com/), All required configuration settings are included in the [`./auth.py`](./auth.py)
```
AUTH0_DOMAIN = 'fsnd-class.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'developer'
```

## Content
1. [Roles](#Roles)
2. [Permissions](#Permissions)
3. [Permission Claims](#Permission_claims)
4. [Quality Assurance](#Quality-Assurance)

<a name="Role"></a>

## Roles
* User
* Manager

<a name="Permissions"></a>

## Permissions
A total of 20 permissions are specified:
* Creation permissions
  - can `post:interview`
  - can `post:pet`
  - can `post:breed`
  - can `post:specie`
* Viewing permissions
  - can `get:interviews`
  - can `get:interview`
  - can `get:pet`
  - can `get:all-adopted-pets`
  - can `get:all-interviews`
  - can `get:all-breeds`
  - can `get:all-species`
* Updating permissions
  - can `patch:interview`
  - can `patch:pet`
  - can `patch:breed`
  - can `patch:specie`
* Deleting permissions
  - can `delete:interview`
  - can `delete:pet`
  - can `delete:breed`
  - can `delete:specie`

<a name="Permission_claims"></a>

## Permission Claims
### User:
  - can `post:interview`
  - can `get:interviews`
  - can `get:interview`
  - can `get:pet`
  - can `patch:interview`
  - can `delete:interview`

### Manager:
  - can `post:pet` 
  - can `post:specie`
  - can `post:breed` 
  - can `get:pet`
  - can `get:all-adopted-pets`
  - can `get:all-interviews`
  - can `get:all-breeds`
  - can `get:all-species`
  - can `patch:pet`
  - can `patch:breed`
  - can `patch:specie`
  - can `delete:pet`
  - can `delete:breed`
  - can `delete:specie`

<a name="Quality-Assurance"></a>

## Quality Assurance
A collection has been created for testing the endpoints with [Postman](https://getpostman.com).

Import the file into Postman to run the tests. Adjust the values of the variables HOST and the Tokens where appropraite.