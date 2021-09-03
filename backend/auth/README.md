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
A total of 18 permissions are specified:
* Creation permissions
  - can `post:interview`
  - can `post:pet`
  - can `post:breed`
  - can `post:specie`
* Viewing permissions
  - can `get:interviews`
  - can `get:pets-detail`
  - can `get:all-adopted-pets`
  - can `get:all-Interviews`
  - can `get:all-breed`
  - can `get:all-specie`
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
`get:pets-detail` is apointed to both the User and the Shelter's Manager.
* All
  - can `get:all-pets`
  - can `get:search`
  - can `get:/`
* User
  - can `get:interviews`
  - can `post:interview`
  - can `get:pets-detail`
  - can `patch:interview`
  - can `delete:interview`
* Manager
  - can `post:pet` ✔️
  - can `post:specie` ✔️
  - can `post:breed` ✔️
  - can `get:pet`✔️
  - can `get:all-adopted-pets`
  - can `get:all-Interviews`
  - can `get:all-breed`
  - can `get:all-specie`
  - can `patch:pet`✔️
  - can `patch:breed`✔️
  - can `patch:specie`✔️
  - can `delete:pet`✔️
  - can `delete:breed`✔️
  - can `delete:specie`✔️


## The `@requres_auth` Decorator
A custom @requires_auth decorator is completed in [`./auth.py`](./auth.py)
##### Get the Authorization header from the request.
##### Take an argument to describe the action (i.e., @require_auth(‘create:drink’).
##### Decode and verify the JWT using the Auth0 secret.
Raise an error if:
- The token is expired.
- The claims are invalid.
- The token is invalid.
- The JWT doesn’t contain the proper action (i.e. create: drink).


### Quality Assurance
Endpoints were tested with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./ASR_RBAC.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!
