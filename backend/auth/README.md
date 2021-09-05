# Role-Based Access Control
Authentication and Authorization is implemented using [Auth0](https://auth0.com/), All required configuration settings are included in the [`./auth.py`](./auth.py)
```
AUTH0_DOMAIN = 'fsnd-class.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'developer'
```
## Roles
* User
* Manager
## Permission
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
## RBAC permission claims
### User:

  - can `post:interview` <-- test
  - can `get:interviews`
  - can `get:interview`
  - can `get:pet`
  - can `patch:interview` <-- test
  - can `delete:interview`

### Manager:
can do what the user can do, additionally:

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


### Quality Assurance
Endpoints were tested with [Postman](https://getpostman.com).
   - 2 users are registered one as a User and the other as a Manager.
   
   
   
   
   
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./ASR_RBAC.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!
