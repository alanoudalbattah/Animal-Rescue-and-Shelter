import unittest, json
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
        self.client().post('/specie', data=json.dumps({'specie':'Cat'}), headers={'Content-Type': 'application/json'})


    """
    TODO 
    Write at least one test for each test for successful operation and for expected errors.
    """
    '''
        POST routes unittest
    ''' 
    '''
        1- (specie) test creation of species can be ['Cat', 'Dog'] ✅
    ''' 
    #* test successful operation for creating a specie using POST /specie
    def test_200_create_specie(self):

        self.reset_database()

        all_species_before = len(Specie.query.all())

        res = self.client().post('/specie', data=json.dumps({'specie':'Dog'}), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)


        all_species_after = len(Specie.query.all())

        # check if an inance is added on species table
        self.assertTrue(all_species_after - all_species_before == 1)
        
        # test status code and message
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['newSpecie'], {'id': 1, 'name': 'Dog'})
    
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
    
    # '''
    #     2-
    # ''' 
    # #* test successful operation for creating a breed using POST /breed
    # def test_200_create_breed(self):
    #     all_interviews_before = len(Adoption_Interview.query.all())
        
    #     user = User()
    #     pet = Pet()
    #     interview_2b_created = Adoption_Interview("","","","")

    # #! test unsuccessful operation for creating a breed using POST /breed
    # def test_400_create_breed(self):
    #     all_interviews_before = len(Adoption_Interview.query.all())

    # '''
    #     3-
    # ''' 
    # #* test successful operation for creating a pet using POST /pet
    # def test_200_create_pet(self):
    #     all_interviews_before = len(Adoption_Interview.query.all())
        
    #     user = User()
    #     pet = Pet()
    #     interview_2b_created = Adoption_Interview("","","","")

    # #! test unsuccessful operation for creating a pet using POST /pet
    # def test_400_create_pet(self):
    #     all_interviews_before = len(Adoption_Interview.query.all())

    # '''
    #     4-
    # ''' 
    # #* test successful operation for creating an interview using POST /interview
    # def test_200_create_interview(self):
    #     all_interviews_before = len(Adoption_Interview.query.all())
        
    #     user = User()
    #     pet = Pet()
    #     interview_2b_created = Adoption_Interview("","","","")

    # #! test unsuccessful operation for creating an interview using POST /interview
    # def test_400_create_interview(self):
    #     all_interviews_before = len(Adoption_Interview.query.all())
 



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
        
        # test status code and responce
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['all species']) != -1)

    #! test unsuccessful operation for viewing all species using GET /all-species
    def test_403_view_all_species(self):
        pass
        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX# ! test unauthorized access later 
    
    '''
        1- (specie) test view specie by id
    ''' 
    #* test successful operation for viewing specie by id using GET /specie/<int:_id>
    def test_200_view_specie_byID(self):
        
        self.create_temp_specie()
        
        avalible_id = (Specie.query.first()).id 

        res = self.client().get('/specie/'+str(avalible_id))
        
        # test status code
        self.assertEqual(res.status_code, 200)

    #! test unsuccessful operation for viewing specie by id out of boundary using GET /specie/<int:_id>
    def test_404_view_specie_byID(self):

        res = self.client().get('/specie/8')

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
        
        self.create_temp_specie()

        avalible_specie = Specie.query.one_or_none()

        res = self.client().patch('/specie/'+str(avalible_specie.id), data=json.dumps({'name':'Dog'}), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)
        
        # test status code
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['specie'],  {'id': avalible_specie.id, 'name':'Dog'} )

    #! test unsuccessful operation for updating specie by id name not acceptable using  PATCH /specie/<int:_id>
    def test_400_update_specie_byID(self):
        
        avalible_id = (Specie.query.first()).id 

        res = self.client().patch('/specie/'+str(avalible_id), data=json.dumps({'name':'Fish'}), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)
        
        # test status code
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'specie name is not acceptable')
    
    
    '''
        DELETE routes unittest
    '''  
    '''
        1- (specie) test delete specie by id
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
    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()