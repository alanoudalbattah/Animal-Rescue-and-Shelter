from datetime import date, time
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from database.models import (
 setup_db, db_drop_and_create_all,
 User, Adoption_Interview, 
 Specie, Breed, Pet,
)

def create_app():
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  """ uncomment at the first time running the app """
  #db_drop_and_create_all()


  @app.route('/', methods=['GET'])
  def healthy(): 
    return jsonify({"status":"Healthy"}),200
  
  #TODO: Endpoints will include at least
    # Two GET requests      ✔️
    # One POST request      ✔️
    # One PATCH request     ✔️
    # One DELETE request    ✔️
  

  ''' ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL'''
  ''' Role --> All can view '''
  @app.route('/all-pets', methods=['GET'])
  def view_all_pets():
    return jsonify({'pets': [pet.details() for pet in Pet.query.all()]}), 200
  
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

    return jsonify({}), 200


  ''' OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER '''
  ''' Role --> only registered users can view '''
  
  
  '''
  @TODO This Endpoint handles Viewing all interviews for a specific user 
       
  '''
  @app.route('/interviews/<int:_user_id>', methods=['GET'])
  def display_user_interviews(_user_id):

    # get the interviews id specific to a certain user form the user id 
    interviews = [interview.id for interview in Adoption_Interview.query.filter(User.id == _user_id).all() ]

    return jsonify({"interviews":interviews}), 200

  '''
  @TODO This Endpoint Creates a new interview for the user 
        #! on future implementation Manager can create an interview for now only the user

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
  def book_interview():
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
    except: abort(400, description="interview already exists")
    
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
  def view_upcoming_interviews(_id):
    
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
    


  ''' CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT '''
  ''' Role --> only shelter employee (manager) '''
  ''' 
    @TODO This Endpoint Creates a new Cat 
    Role: Manager
    Permtions: C in CRUD
  '''

  
  '''
  @TODO This Endpoint view all previous and upcomming interviews
  '''
  @app.route('/all-Interviews', methods=['GET'])
  def view_all_interviews():
    return jsonify({'all interviews': [Adoption_Interview.details(interview) for interview in Adoption_Interview.query.all()]}), 200



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
  def create_cat_information():

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
    newPet.insert()
    

    return jsonify({"details":Pet.query.get(newPet.id).details()}), 201
  
  
  '''
  @TODO This Endpoint Creates a new breed
        - body
        {
          "specie":"Dog",
        }
  '''
  @app.route('/specie', methods=['POST'])
  def create_new_specie():
    body = request.get_json()
    
    if not('specie' in body): abort(400, description='specie is not included in the body')
    
    specieName = body.get('specie')

    #check if specie already exists in the database
    simmilar = Specie.name.ilike(f'%{specieName}%')
    specie = Specie.query.filter(simmilar).first()# search is case insensitive :)  
    if (specie): abort(400, description='specie name already exists')

    # verify specie name
    possible_animals_verify = ["Cat","Dog","Genuine Pig"] #options possiple for now 
    if possible_animals_verify.index(specieName) != -1:
       newSpecie = Specie(specieName)
       newSpecie.insert()
    
    else: abort(400, description='specie name is wrong')

    return jsonify({'newSpecie':newSpecie.details()}), 201
  '''
  @TODO This Endpoint Creates a new breed
        - body
        {
          "specie":"Dog",
          "breed":"Hzzz"
        }
  '''
  @app.route('/breed', methods=['POST'])
  def create_new_breed():

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
    
    try:
      newBreed.insert()
    except:
      abort(400, description='constraint violation could not be created') 
    return jsonify({'newBreed':newBreed.details()}), 201


  ''' 
    @TODO This Endpoint View, Update, or Delete a Pet 
        - body - PATCH only
        {
            "breed": "hamalaya"
            "name": "Hamoosh"
        }

  '''
  @app.route('/pet/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  def pet_cat(_id):
    
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
      pet.delete()
      return jsonify({'pet_id':_id}), 200
    
    else: return jsonify({'pet':pet.details()}), 200
  
  ''' 
    @TODO This Endpoint View, Update, or Delete a breed 
        - body - PATCH only
        {
            "name": "hamalaya"
        }

  '''
  @app.route('/breed/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  def breed(_id):

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
      breed.delete()
      return jsonify({"breed_id":_id}), 200

    else: return jsonify({"breed details":breed.details()}), 200
  
  ''' 
    @TODO This Endpoint View, Update, or Delete a specie 
        - body - PATCH only
        {
            "name": "Catttttt"
        }

  '''
  @app.route('/specie/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  def specie(_id):

    specie = Specie.query.get_or_404(_id)
    body = request.get_json()

    if request.method == "PATCH": 
      
      if not ('name' in body): abort(400, description='specie is not included in the body')
      
      specie.name = body.get('name')
       

      try:
          specie.update()
      except:
          # unique name constraint violation or charecters extend the limits 
          abort(400, description='constraint violation could not be updated')
      return jsonify({ 'specie':specie.details()}), 200
    elif request.method == "DELETE": 
      specie.delete()
      return jsonify({"specie_id":_id}), 200

    else: return jsonify({"specie details":specie.details()}), 200

    

  ''' 
    @TODO This Endpoint Views all adopted pets

  '''
  @app.route('/all-adopted-pets', methods=['GET'])
  def view_all_adopted_pets():
      return jsonify({'adopted pets': [Pet.details(pet) for pet in Pet.query.all() if pet.pet_owner != None]}), 200

  ''' 
    @TODO This Endpoint Views all breeds

  '''
  @app.route('/all-breeds', methods=['GET'])
  def view_all_breed():
      return jsonify({'all breeds': [Breed.details(b) for b in Breed.query.all()]}), 200

  ''' 
    @TODO This Endpoint Views all speices

  '''
  @app.route('/all-species', methods=['GET'])
  def view_all_specie():
      return jsonify({'all species': [Specie.details(s) for s in Specie.query.all()]}), 200




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


  # '''
  # @TODO implement error handler for AuthError
  #     error handler should conform to general task above
  # '''
  # # src: https://auth0.com/docs/quickstart/backend/python/01-authorization

  # @app.errorhandler(AuthError)
  # def unprocessable(err):
  #     return jsonify({
  #         "success": False,
  #         "error": err.status_code,
  #         "message": err.error.get('description'),
  #     }), err.status_code

  return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8080, debug=True)