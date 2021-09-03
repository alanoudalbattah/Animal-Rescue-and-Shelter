from flask import Flask, request, abort, jsonify, flash
from flask_cors import CORS

from database.models import (
 setup_db, db_drop_and_create_all, db,
 Owner, Adoption_Interview, 
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
    # Two GET requests 
    # One POST request 
    # One PATCH request 
    # One DELETE request 
  

  ''' ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL ALL'''
  ''' Role --> All can view '''
  @app.route('/all-pets', methods=['GET'])
  def view_all_pets():
    return jsonify({'pets': [Pet.details(cat) for cat in Pet.query.all()]}), 200
  

  @app.route('/search', methods=['POST'])
  def search():

    # by Breed

    # by gender 
  
    # by age

    # Vaccinated Constrant

    # Letter Box Trained Constrant

    return jsonify({}), 200


  ''' OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER OWNER '''
  ''' Role --> only registered users can view '''
  '''
  @TODO This Endpoint Creates a new interview 
        - body
        {
            "something": "something",
        }
  '''
  @app.route('/Interviews', methods=['POST'])
  def book_interviews():
    #! --
    return jsonify({}), 201

  @app.route('/Interviews', methods=['GET', 'PATCH', 'DELETE'])
  def view_upcoming_interviews(interview_id):
    return jsonify({}), 200



  ''' CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT CAT '''
  ''' Role --> only shelter employee (manager) '''
  ''' 
    @TODO This Endpoint Creates a new Cat 
    Role: Manager
    Permtions: C in CRUD
  '''

  
  '''
  @TODO This Endpoint view all previous and upcomming
  '''
  @app.route('/all-Interviews', methods=['GET'])
  def view_all_interviews():
    return jsonify({}), 200



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
      if not(breed): abort(404)
      
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
      if (required == None): abort(400) 

    
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
    newBreed.insert()

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
        pet.breed = breedName

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

    else: return jsonify({}), 200
  
  ''' 
    @TODO This Endpoint View, Update, or Delete a specie 
        - body - PATCH only
        {
            "specie": "Catttttt"
        }

  '''
  @app.route('/specie/<int:_id>', methods=['GET', 'PATCH', 'DELETE'])
  def specie(_id):

    specie = Specie.query.get_or_404(_id)
    body = request.get_json()

    if request.method == "PATCH": 
      
      if ('specie' in body): 
        specie.name = body.get('name')
      else: abort(400, description='specie is not included in the body')

      try:
          specie.update()
      except:
          # unique name constraint violation or charecters extend the limits 
          abort(400, description='constraint violation could not be updated')
      return jsonify({ 'specie':specie.details()}), 200
    elif request.method == "DELETE": 
      specie.delete()
      return jsonify({"specie_id":_id}), 200

    else: return jsonify({}), 200

    


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