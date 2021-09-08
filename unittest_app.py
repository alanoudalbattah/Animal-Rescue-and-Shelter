import unittest, json
import catnames as names
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from db.models import (
 setup_db, db_drop_and_create_all, db,
 User, Adoption_Interview, 
 Specie, Breed, Pet)

''' This Class represents the API and db Models test case'''
class AnimalShelter(unittest.TestCase):

    def setUp(self):
        
        # bind a flask application and a SQLAlchemy service
        self.app = create_app() 
        self.client = self.app.test_client
        
        self.database_name = "animal_shelter_test"
        self.database_path = "postgresql://postgres:postgres@{}/{}".format('localhost:5432', self.database_name)
        
        # binds the app to the current context
        with self.app.app_context():
            setup_db(self.app, self.database_path)
        
        
    def tearDown(self):
        pass
    
    '''

        helper methods

    '''
    def reset_database(self):
        db_drop_and_create_all() 

    def create_temp_specie(self):
        return self.client().post('/specie', data=json.dumps({'specie':'Cat'}), headers={'Content-Type': 'application/json'})
    
    def create_temp_breed(self, name=names.gen()):
        self.create_temp_specie()
        return self.client().post('/breed', data=json.dumps(
                  
        {
            'specie': 'Cat',
            'breed': name
        }
        
        ), headers={'Content-Type': 'application/json'})

    def create_temp_pet(self, name=names.gen()):
        self.create_temp_breed()
        return self.client().post('/pet', data=json.dumps(
                  
        {
            "breed": (Breed.query.first()).name,
            "name": name,
            "image_link": "https://someImageURL.com",
            "age_in_months": 155,
            "gender": "female",
            "vaccinated": True,
            "letter_box_trained": True,
            "note": "Likes to sleep :) and play with lazerz :)"
        }
        
        ), headers={'Content-Type': 'application/json'})

    def create_temp_user(self, firstname=names.gen(), email=None):
        lastname = names.gen()
        if email is None:
            email = firstname+lastname+"@gmail.com"
        return self.client().post('/user', data=json.dumps(
        {
            "first_name":firstname,
            "last_name":lastname,
            "email":email,
            "mobile": "054211111",
            "age": 23
        }
        ), headers={'Content-Type': 'application/json'})


    def create_temp_interview(self, pet_id=None, user_id=None):
        
        if pet_id is None:
            self.create_temp_pet()
            pet_id = (Pet.query.first()).id
        if user_id is None:
            self.create_temp_user()
            user_id = (User.query.first()).id

        return self.client().post('/interview', data=json.dumps(
        {
            "pet_id": pet_id,
            "user_id": user_id,
            "year": 2021,
            "month": 2,
            "day": 2,
            "hour": 1,
            "minute": 0
        }
        ), headers={'Content-Type': 'application/json'})

    """
    TODO 
    Write at least one test for each test for successful operation and for expected errors.
    """
    '''
        POST routes unittest
    ''' 
    '''
        1- (specie) test creation of species can be ['Cat', 'Dog']
    ''' 
    #* test successful operation for creating a specie using POST /specie
    def test_200_create_specie(self):

        self.reset_database()

        all_species_before = len(Specie.query.all())

        res = self.create_temp_specie()

        data = json.loads(res.data)


        all_species_after = len(Specie.query.all())

        # check if an inance is added on species table
        self.assertTrue(all_species_after - all_species_before == 1)
        
        # test status code and message
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['newSpecie'], {'id': 1, 'name': 'Cat'})
    
    #! test unsuccessful operation for creating a specie using POST /specie
    def test_400_create_specie(self):

        all_species_before = len(Specie.query.all())

        res = self.client().post('/specie', data=json.dumps({'specie':'Fish'}), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)


        all_species_after = len(Specie.query.all())

        # check if an inance is not added on species table
        self.assertTrue(all_species_after - all_species_before == 0)
        
        # test status code and message
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'specie name is not acceptable')
    '''
        1- (breed) test creation of breed
    ''' 
    #* test successful operation for creating a breed using POST /specie
    def test_200_create_breed(self):

        self.reset_database()

        res = self.create_temp_breed()
        
        # test status code and message
        self.assertEqual(res.status_code, 201)
    
    #! test unsuccessful operation for creating a specie using POST /specie
    def test_400_create_breed(self):

        breed_name_taken = (Breed.query.first()).name

        res = self.create_temp_breed(breed_name_taken)
        
        # test status code and message
        self.assertEqual(res.status_code, 400)
    
    # '''
    #     3- (pet) test creation of pet
    # ''' 
    #* test successful operation for creating a pet using POST /pet
    def test_200_create_pet(self):
        
        self.reset_database()

        all_pets_before = len(Pet.query.all())

        res = self.create_temp_pet()

        all_pets_after = len(Pet.query.all())

        # check if an inance is added on species table
        self.assertTrue(all_pets_after - all_pets_before == 1)
        
        # test status code and message
        self.assertEqual(res.status_code, 201)


    #! test unsuccessful operation for creating a pet using POST /pet
    def test_400_create_pet(self):
        
        self.create_temp_pet('Kitkat')

        res = self.create_temp_pet('Kitkat')
        
        # test status code and message
        self.assertEqual(res.status_code, 400)
 
    # '''
    #     4- (user) test creation of user
    # ''' 
    # #* test successful operation for creating a user using POST /user
    def test_200_create_user(self):
        all_users_before = len(User.query.all())

        res = self.create_temp_user()

        all_users_after = len(User.query.all())

        # check if an inance is added on species table
        self.assertTrue(all_users_after - all_users_before == 1)
        
        # test status code and message
        self.assertEqual(res.status_code, 201)

    # #! test unsuccessful operation for creating a user using POST /user
    def test_400_create_user(self):
        unique_user_email_conflict = "conflict@gmail.com"

        self.create_temp_user(unique_user_email_conflict)

        res = self.create_temp_user(unique_user_email_conflict)
        
        # test status code and message
        self.assertEqual(res.status_code, 400)
    # '''
    #     5- (interview) test creation of interview
    # ''' 
    # #* test successful operation for creating an interview using POST /interview
    def test_200_create_interview(self):

        res = self.create_temp_interview()

        # test status code and message
        self.assertEqual(res.status_code, 201)

    # #! test unsuccessful operation for creating an interview using POST /interview
    def test_400_create_interview(self): 

        self.create_temp_pet()
        self.create_temp_user()
        
        conflict_pet_id = (Pet.query.first()).id
        conflict_user_id = (User.query.first()).id

        self.create_temp_interview(conflict_pet_id, conflict_user_id)

        res = self.create_temp_interview(conflict_pet_id, conflict_user_id)
        
        # test status code and message
        self.assertEqual(res.status_code, 400)



    '''
        GET routes unittest
    '''      
    '''
        1- (specie) test view all-species 
    ''' 
    #* test successful operation for viewing all species using GET /all-species
    def test_200_view_all_species(self):

        res = self.client().get('/all-species')
        
        data = json.loads(res.data)

        # test if the pagination is correct and if it dose not exceed 10 
        self.assertTrue(len(data['all species']) <= 10)
        
        # test status code and responce
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['all species']) != -1)

    #! test unsuccessful operation for viewing all-species using GET /species
    def test_404_view_all_species(self):
        
        res = self.client().get('/species')

        # test status code and message
        self.assertEqual(res.status_code, 404)

    '''
        2- (breed) test view all-breeds
    ''' 
    #* test successful operation for viewing all breeds using GET /all-breeds
    def test_200_view_all_breeds(self):

        res = self.client().get('/all-breeds')
        data = json.loads(res.data)

        # test if the pagination is correct and if it dose not exceed 10 
        self.assertTrue(len(data['all breeds']) <= 10)
        
        # test status code and responce
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['all breeds']) != -1)

    #! test unsuccessful operation for viewing all breeds using GET /all-breeds
    def test_404_view_all_breeds(self):
        
        res = self.client().get('/all-breeds?page=50')
        data = json.loads(res.data)

        # test status code and message
        self.assertEqual(res.status_code, 404)
    
    '''
        1- (specie) test view specie by id
    ''' 
    #* test successful operation for viewing specie by id using GET /specie/<int:_id>
    def test_200_view_specie_byID(self):
        
        self.create_temp_specie()
        
        avalible_specie = (Specie.query.first())

        res = self.client().get('/specie/'+str(avalible_specie.id))
        
        # test status code
        self.assertEqual(res.status_code, 200)

    #! test unsuccessful operation for viewing specie by id out of boundary using GET /specie/<int:_id>
    def test_404_view_specie_byID(self):

        res = self.client().get('/specie/8')

        # test status code
        self.assertEqual(res.status_code, 404)

    '''
        1- (breed) test view specie by id
    ''' 
    #* test successful operation for viewing specie by id using GET /breed/<int:_id>
    def test_200_view_breed_byID(self):
        
        self.create_temp_breed()
        
        avalible_breed = (Breed.query.first())

        res = self.client().get('/breed/'+str(avalible_breed.id))
        
        # test status code
        self.assertEqual(res.status_code, 200)

    #! test unsuccessful operation for viewing breed by id out of boundary using GET /breed/<int:_id>
    def test_404_view_breed_byID(self):

        res = self.client().get('/breed/8')

        # test status code
        self.assertEqual(res.status_code, 404)
              

    #* test successful operation for viewing all pets using GET /all-pets
    # def test_200_view_pets(self):
    #     res = self.client().get('/all-pets')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)

    # #! test unsuccessful operation for creating an interview using POST /interview
    # def test_404_view_pets(self):
    #     res = self.client().get('/all-pets?page=50')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)

    
    '''
        PATCH routes unittest
    '''  
    '''
        1- (specie) test update specie by id
    ''' 
    #* test successful operation for updating specie by id using PATCH /specie/<int:_id>
    def test_200_update_specie_byID(self):
        
        avalible_id = (Specie.query.first()).id 

        res = self.client().patch('/specie/'+str(avalible_id), data=json.dumps({'name':'Dog'}), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)
        
        # test status code
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['specie'],  {'id': avalible_id, 'name':'Dog'} )

    #! test unsuccessful operation for updating specie by id name not acceptable using  PATCH /specie/<int:_id>
    def test_400_update_specie_byID(self):
        
        avalible_id = (Specie.query.first()).id 

        res = self.client().patch('/specie/'+str(avalible_id), data=json.dumps({'name':'Fish'}), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)
        
        # test status code
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'specie name is not acceptable')

    '''
        2- (breed) test update breed by id
    ''' 
    #* test successful operation for updating breed by id using PATCH /breed/<int:_id>
    def test_200_update_breed_byID(self):
        
        self.create_temp_specie()
        self.create_temp_breed()
        

        avalible_breed = Breed.query.first()
        avalible_specie = Specie.query.first()

        res = self.client().patch('/breed/'+str(avalible_breed.id), data=json.dumps({'specie_id':avalible_specie.id}), headers={'Content-Type': 'application/json'})        
        data = json.loads(res.data)
        
        # test status code
        self.assertEqual(res.status_code, 200)

    #! test unsuccessful operation for updating (breed by id)'s atribute specie_id to an id out of boundary using PATCH /breed/<int:_id>
    def test_400_update_breed_byID(self):

        avalible_id = (Breed.query.first()).id 

        res = self.client().patch('/breed/'+str(avalible_id), data=json.dumps({'specie_id':'8'}), headers={'Content-Type': 'application/json'})        
        # test status code
        self.assertEqual(res.status_code, 400)
    
    
    '''
        DELETE routes unittest
    '''  
    '''
        1- (specie) test delete breed by id
    ''' 
    #* test successful operation for deleting specie by id using DELETE /specie/<int:_id>
    def test_200_delete_specie_byID(self):

        self.create_temp_specie()

        avalible_id = (Specie.query.first()).id 

        res = self.client().delete('/specie/'+str(avalible_id))
 
        # test status code
        self.assertEqual(res.status_code, 200)

    #! test unsuccessful operation for deleting specie by id out of boundary DELETE /specie/<int:_id>
    def test_404_delete_specie_byID(self):

        res = self.client().delete('/specie/8')
 
        # test status code
        self.assertEqual(res.status_code, 404)
    '''
        2- (breed) test delete specie by id
    ''' 
    #* test successful operation for deleting breed by id using DELETE /breed/<int:_id>
    def test_200_delete_breed_byID(self):

        self.create_temp_breed()

        avalible_id = (Breed.query.first()).id 

        res = self.client().delete('/breed/'+str(avalible_id))
 
        # test status code
        self.assertEqual(res.status_code, 200)

    #! test unsuccessful operation for deleting breed by id out of boundary DELETE /breed/<int:_id>
    def test_404_delete_breed_byID(self):

        res = self.client().delete('/breed/8')
 
        # test status code
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()