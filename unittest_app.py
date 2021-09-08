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

        setup_db(self.app, self.database_path)
        db_drop_and_create_all()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()
        # src: Udacity's Travia Api Project
    
    def tearDown(self):
        pass
         
    

    """
    TODO 
    Write at least one test for each test for successful operation and for expected errors.
    """
    '''
        POST routes unittest
    ''' 
    '''
        1- test creation of species can be ['Cat', 'Dog'] ✅
    ''' 
    #* test successful operation for creating a specie using POST /specie
    def test_200_create_specie(self):

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
    # def test_400_create_specie(self):

    #     all_species_before = len(Specie.query.all())

    #     res = self.client().post('/specie', data=json.dumps({'specie':'Fish'}), headers={'Content-Type': 'application/json'})
    #     data = json.loads(res.data)


    #     all_species_after = len(Specie.query.all())

    #     # check if an inance is not added on species table
    #     self.assertTrue(all_species_after - all_species_before == 0)
        
    #     # test status code and message
    #     self.assertEqual(res.status_code, 400)
    #     # self.assertEqual(data['message'], 'specie name is not acceptable')
    
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
        1-
    ''' 
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
        DELETE routes unittest
    '''  



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()