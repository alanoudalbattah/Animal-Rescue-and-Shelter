from datetime import date, time
from flask import (Flask, 
request, render_template,
abort, jsonify)
from flask_cors import CORS
from flask_migrate import Migrate
from db.models import (
 setup_db, db_drop_and_create_all, db,
 User, Adoption_Interview, 
 Specie, Breed, Pet,
)
from auth.auth import AuthError, requires_auth



# from functools import wraps
# import json
# from os import environ as env
# from werkzeug.exceptions import HTTPException

# from dotenv import load_dotenv, find_dotenv
# from flask import Flask
# from flask import jsonify
# from flask import redirect
# from flask import render_template
# from flask import session
# from flask import url_for
# from authlib.integrations.flask_client import OAuth
# from six.moves.urllib.parse import urlencode



# def requires_auth(f):
#   @wraps(f)
#   def decorated(*args, **kwargs):
#     if 'profile' not in session:
#       # Redirect to Login page here
#       return redirect('/')
#     return f(*args, **kwargs)

#   return decorated

QUESTIONS_PER_PAGE = 10

def create_app():
  # create and configure the app
  app=Flask(__name__)
  setup_db(app)
  CORS(app)
  Migrate(app, db)
  
  """ uncomment at the first time running the app """
  #db_drop_and_create_all()


  @app.route('/', methods=['GET'])
  def index(): 
    return render_template('index.html')
  
  #TODO: Endpoints will include at least
    # Two GET requests      ✔️
    # One POST request      ✔️
    # One PATCH request     ✔️
    # One DELETE request    ✔️
  

  '''
  @TODO This Endpoint Creates a new user 
        #! Auth0 ?
        - body
  {
      "first_name":"alanoud",
      "last_name":"albattah",
      "email":"alanoudalbattah@outlook.com",
      "mobile": "054211111",
      "age": 23
  }
  '''
  @app.route('/user', methods=['POST'])
  def create_user():

    body = request.get_json()

    # required pet informations
    required_data = [
      body.get('email'),
      body.get('mobile')
      ]
    
    # checks if all required fields are present
    for required in required_data: 
      if (required == None): abort(400, description='required feild is missing') 

    
    newUser = User(
      body.get('first_name'),
      body.get('last_name'),
      required_data[0],
      required_data[1],
      body.get('age')
      )
  
    try: newUser.insert()
    except: abort(400, description='constraint violation could not be created')
    
    return jsonify({"details":User.query.get(newUser.id).details()}), 201



  ''' ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL'''
  ''' Role --> All can view '''
  @app.route('/all-pets', methods=['GET'])
  def view_all_pets():
    
      #* Implement pagniation
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE

      total_pets = [p.details() for p in Pet.query.all()]
      paginated_pets = total_pets[start:end]

      if (len(paginated_pets)==0): abort(404) # abort if no questions were formatted (no need for a new page)!

      return jsonify({'pets': paginated_pets}), 200

  ''' Role --> All can search '''
  #! This route is not functional or implemented in the maintime
  #! left undeleted for future implementations. :)
  @app.route('/search', methods=['POST'])
  def search():
    #! --

    # by Breed

    # by gender 
  
    # by age

    # Vaccinated Constrant

    # Letter Box Trained Constrant

    pass

  ''' Role --> All manager can assign '''
  #! This route is not functional or implemented in the maintime
  #! left undeleted for future implementations. :)
  @app.route('/assign', methods=['POST'])
  def assign_owner_to_pet():
    pass

  ''' Role --> only registered users can view '''
    
  '''
  @TODO This Endpoint handles Viewing all interviews for a specific user 
       
  '''
  @app.route('/interviews/<int:_user_id>', methods=['GET'])
  @requires_auth('get:interviews')
  def display_user_interviews(payload, _user_id):
    return jsonify({"interviews":[interview.id for interview in Adoption_Interview.query.filter(User.id == _user_id).all() ]}), 200

  '''
  @TODO This Endpoint Creates a new interview for the user 
        #! on future implementation Manager can create an interview for now only the user can do that

        - body
  {
      "pet_id": 0,
      "user_id": 0,
      "year": 2021,
      "month": 9,
      "day": 3,
      "hour": 11,
      "minute": 30
  }
  '''
  @app.route('/interview', methods=['POST'])
  @requires_auth('post:interview')
  def book_interview(payload):
    body = request.get_json()
    
    # check if required fields are present
    if not ('pet_id' in body or 'user_id' in body): 
      abort(400, description="pet or user are missing")

    # from body take the id valued
    pet_id = body.get('pet_id')
    user_id = body.get('user_id')

    # fetch instance from db
    pet = Pet.query.get(pet_id)
    user = User.query.get(user_id)

    # check if both instance exists
    if (pet==None or user==None): abort(400, description="pet or user are missing from the db")

    
    # required interview informations
    required_data = [
      body.get('year'),
      body.get('month'),
      body.get('day'),
      body.get('hour'),
      body.get('minute'),
      ]
    
    # checks if all required fields are present
    for required in required_data: 
      if (required == None): abort(400, description='required feild is missing') 
    
    # d = datetime.date(2019, 4, 13)
    # output --> 2019-04-13
    date_object = date(required_data[0], required_data[1], required_data[2])
    ## time(hour, minute and second)
    # c = time(hour = 11, minute = 34, second = 56)
    # output --> c = 11:34:56
    datetime_object = time(required_data[3], required_data[4], 0)
    #src: https://www.programiz.com/python-programming/datetime


    # create an interview obj
    new_interview = Adoption_Interview(date_object,datetime_object)
    new_interview.pet_2b_adopted = pet
    new_interview.potential_owner = user

    try:
      new_interview.insert()
    except: 
       abort(400, description="interview already exists")
    
    return jsonify({"new_interview":new_interview.details()}), 201


  '''
  @TODO This Endpoint handles Viewing, updating, and deleting the interview 

    #! on future implementation Manager can update pet or user 
            - body - PATCH only
  {
      "year": 2021,
      "month": 9,
      "day": 3,
      "hour": 11,
      "minute": 30
  }
       
  '''
  @app.route('/interview/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  @requires_auth('delete:interview')
  def view_upcoming_interviews(payload, _id):
    
    interview = Adoption_Interview.query.get_or_404(_id)

    if request.method == "PATCH": 

      body = request.get_json()
      
      # update interview date or time only for now
      if ('year' in body):
        interview.date = date(body.get('year'), interview.date.month, interview.date.day)
      if ('month' in body):
        interview.date = date(interview.date.year, body.get('month'), interview.date.day)
      if ('day' in body):
        interview.date = date(interview.date.year, interview.date.month, body.get('day'))
      
      if ('hour' in body):
        interview.time = time(body.get('hour'), interview.time.minute, 0)
      if ('minute' in body):
        interview.time = time(interview.time.hour, body.get('minute'), 0)

      try:
          interview.update()
      except:
          # unique name constraint violation
          abort(400, description='constraint violation could not be updated')

      return jsonify({'interview updated':interview.details()}), 200

    elif request.method == "DELETE":
      interview.delete()
      return jsonify({'interview_id':_id}), 200
    
    else: return jsonify({"interview details":interview.details()}), 200
    




  ''' #TODO Role --> only shelter employee (manager) '''

  '''
    interviews
  '''
  '''
  @TODO This Endpoint view all previous and upcomming interviews
  '''
  @app.route('/all-interviews', methods=['GET'])
  @requires_auth('get:all-Interviews')
  def view_all_interviews(payload):
    return jsonify({'all interviews': [Adoption_Interview.details(interview) for interview in Adoption_Interview.query.all()]}), 200


  '''
    Pet
  '''

  '''
  @TODO This Endpoint Creates a new pet post for adoption 
        - body
        {
            "breed": "hamalaya",
            "name": "Hamoosh",
            "image_link": "image_link",
            "age_in_months": 120,
            "gender": "Male",
            "vaccinated": true,
            "letter_box_trained": true,
            "note": "Likes to play with lazerz :)"
        }
  '''
  @app.route('/pet', methods=['POST'])
  @requires_auth('post:pet')
  def create_cat_information(payload):

    body = request.get_json()

    # breed must be specified and found in the db 
    if 'breed' in body:
      search_term = body.get('breed')
      breed = Breed.query.filter(Breed.name.ilike(f'%{search_term}%')).first()# search is case insensitive :)  
      if not(breed): abort(400, description="breed name not avalible, please create one")
      
    # required pet informations
    required_data = [
      body.get('name'),
      body.get('image_link'),
      body.get('age_in_months'),
      body.get('gender'), 
      body.get('vaccinated'),
      body.get('letter_box_trained')
      ]
    
    # checks if all required fields are present
    for required in required_data: 
      if (required == None): abort(400, description='required feild is missing') 

    
    newPet = Pet(
      required_data[0],
      required_data[1],
      required_data[2],
      required_data[3],
      required_data[4],
      required_data[5],
      body.get('note')
      )

    newPet.breed = breed

    try: newPet.insert()
    except: abort(400, description='constraint violation could not be created')
    

    return jsonify({"details":Pet.query.get(newPet.id).details()}), 201


  ''' 
    @TODO This Endpoint Views all adopted pets

  '''
  @app.route('/all-adopted-pets', methods=['GET'])
  @requires_auth('get:all-adopted-pets')
  def view_all_adopted_pets(payload):
      return jsonify({'adopted pets': [Pet.details(pet) for pet in Pet.query.all() if pet.pet_owner != None]}), 200


  ''' 
    @TODO This Endpoint View, Update, or Delete a Pet 
        - body - PATCH only
        {
            "breed": "hamalaya"
            "name": "Hamoosh"
        }

  '''
  @app.route('/pet/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  @requires_auth('post:pet') # other permmisions dose the same maybe i should delete them? 'patch:pet', 'delete:pet'
  def pet_cat(payload, _id):
    
    pet = Pet.query.get_or_404(_id)
    
    if request.method == "PATCH": 

      body = request.get_json()

      if ('breed' in body): 
        breedName = body.get('breed')
        # look for breed 
        breed = Breed.query.filter(Breed.name.ilike(f'%{breedName}%')).first()# search is case insensitive :)  
        if not (breed): abort(400, description='breed name is incorrect')
        # if it exists ...
        pet.breed = breed

      #only update whats provided on the body
      if ('name' in body): 
        pet.name = body.get('name')
      if ('image_link' in body): 
        pet.image_link = body.get('image_link')
      if ('age_in_months' in body):
        pet.age_in_months = body.get('age_in_months') 
      if ('gender' in body): 
        pet.gender = body.get('gender')
      if ('vaccinated' in body):
        pet.vaccinated = body.get('vaccinated') 
      if ('letter_box_trained' in body):
        pet.letter_box_trained = body.get('letter_box_trained') 
      if ('note' in body): 
        pet.note = body.get('note')


      try:
          pet.update()
      except:
          # unique name constraint violation
          abort(400, description='constraint violation could not be updated')

      
      return jsonify({'pet':pet.details()}), 200
    
    elif request.method == "DELETE": 
      
      try: pet.delete()
      except: abort(400, description='constraint violation could not be deleted, maybe there is an interview linked :)')
      
      return jsonify({'pet_id':_id}), 200
    
    else: return jsonify({'pet':pet.details()}), 200
 


  '''
    breed
  '''


  '''
  @TODO This Endpoint Creates a new breed
        - body
        {
          "specie":"Dog",
          "breed":"Hzzz"
        }
  '''
  @app.route('/breed', methods=['POST'])
  @requires_auth('post:breed')
  def create_new_breed(payload):

    body = request.get_json()
    
    if not('specie' in body): abort(400, description='specie is not included in the body')
    specieName = body.get('specie')
    simmilar = Specie.name.ilike(f'%{specieName}%')
    specie = Specie.query.filter(simmilar).first()
    if not('breed' in body): abort(400, description='breed is not included in the body')
    
    breedName = body.get('breed')

    # check if breed already exists in the database
    breed = Breed.query.filter(Breed.name.ilike(f'%{breedName}%')).first()# search is case insensitive :)  
    if (breed): abort(400, description='breed name already exists')

    # for now trust the manager :) and insert ...
    newBreed = Breed(breedName, body.get('image_link'))
    newBreed.specie = specie
    
    try: newBreed.insert()
    except: abort(400, description='constraint violation could not be created') 
    
    return jsonify({'newBreed':newBreed.details()}), 201


  ''' 
    @TODO This Endpoint Views all breeds

  '''
  @app.route('/all-breeds', methods=['GET'])
  @requires_auth('get:all-breeds')
  def view_all_breed(payload):

      #* Implement pagniation
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE

      total_breeds = [Breed.details(b) for b in Breed.query.all()]
      paginated_breeds = total_breeds[start:end]

      if (len(paginated_breeds)==0): abort(404) # abort if no questions were formatted (no need for a new page)!

      return jsonify({'all breeds': paginated_breeds}), 200



  ''' 
    @TODO This Endpoint View, Update, or Delete a breed 
        - body - PATCH only
        {
            "name": "hamalaya"
        }

  '''
  @app.route('/breed/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  @requires_auth('patch:breed')
  def breed(payload, _id):

    breed = Breed.query.get_or_404(_id)
    body = request.get_json()

    if request.method == "PATCH":
      if ('specie_id' in body):
        breed.specie_id = body.get('specie_id')
      elif not ('breed' in body): 
        breed.name = body.get('name')
      else: abort(400, description='nothing to update')
      try:
          breed.update()
      except:
          # unique name constraint violation or charecters extend the limits 
          abort(400, description='constraint violation could not be updated')
 
      return jsonify({'breed':breed.details()}), 200
    
    elif request.method == "DELETE": 
      try:
        breed.delete()
      except:
        abort(400, description='constraint violation could not be deleted, maybe there is a pet linked')
      
      return jsonify({"breed_id":_id}), 200

    else: return jsonify({"breed details":breed.details()}), 200
  

  '''
    Specie
  '''

  '''
  @TODO This Endpoint Creates a new specie
        - body
        {
          "specie":"Dog",
        }
  '''
  @app.route('/specie', methods=['POST'])
  @requires_auth('post:specie')
  def create_new_specie(payload):
    body = request.get_json()
    
    if not('specie' in body): abort(400, description='specie is not included in the body')
    
    specieName = body.get('specie')

    #check if specie already exists in the database
    # search is case insensitive :)  
    specie = Specie.query.filter(Specie.name.ilike(f'%{specieName}%')).first()
    if (specie): abort(400, description='specie name already exists')

    # verify specie name
    # options possiple for now are either Dog or a Cat
    acceptable_names_for_specie = ["Cat","Dog"]
    if not (specieName in acceptable_names_for_specie): 
      abort(400, description='specie name is not acceptable')
    
    newSpecie = Specie(specieName)
    
    try:  
      newSpecie.insert()
    except: 
      abort(400, description='constraint violation could not be created') 
    
    return jsonify({'newSpecie':newSpecie.details()}), 201


  ''' 
    @TODO This Endpoint Views all speices

  '''
  @app.route('/all-species', methods=['GET'])
  @requires_auth('get:all-species')
  def view_all_specie(payload):
      return jsonify({'all species': [Specie.details(s) for s in Specie.query.all()]}), 200
  

  ''' 
    @TODO This Endpoint View, Update, or Delete a specie 
        - body - PATCH only
        {
            "name": "Catttttt"
        }

  '''
  @app.route('/specie/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  @requires_auth('delete:specie')
  def specie(payload, _id):

    specie = Specie.query.get_or_404(_id)
    body = request.get_json()

    if request.method == "PATCH": 
      
      if not ('name' in body): abort(400, description='specie is not included in the body')
      
      specieName = body.get('name')
      # verify specie name
      # options possiple for now are either Dog or a Cat
      acceptable_names_for_specie = ["Cat","Dog"]
      if not (specieName in acceptable_names_for_specie): 
        abort(400, description='specie name is not acceptable')
      
      specie.name = specieName

      try:
          specie.update()
      except:
          # unique name constraint violation or charecters extend the limits 
          abort(400, description='constraint violation could not be updated')
      return jsonify({ 'specie':specie.details()}), 200
    elif request.method == "DELETE": 
      
      try:
        specie.delete()
      except:
        abort(400, description='constraint violation could not be deleted')

      return jsonify({"specie_id":_id}), 200

    else: return jsonify({"specie details":specie.details()}), 200


  ''' Error Handling '''

  @app.errorhandler(422)
  def unprocessable(err):
      return jsonify({
          "success": False,
          "error": 422,
          "message": err.description
      }), 422

  @app.errorhandler(400)
  def unprocessable(err):
      return jsonify({
          "success": False,
          "error": 400,
          "message": err.description
      }), 400


  @app.errorhandler(404)
  def unprocessable(err):
      return jsonify({
          "success": False,
          "error": 404,
          "message": err.description
      }), 404

  @app.errorhandler(500)
  def server_error(err):
      return jsonify({
            "success": False,
            "error": 500,
            "message": err.description
      }), 500


  '''
  @TODO implement error handler for AuthError
      error handler should conform to general task above
  '''
  # src: https://auth0.com/docs/quickstart/backend/python/01-authorization

  @app.errorhandler(AuthError)
  def unprocessable(err):
      return jsonify({
          "success": False,
          "error": err.status_code,
          "message": err.error.get('description'),
      }), err.status_code

  return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8080, debug=True)