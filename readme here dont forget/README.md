# Getting Started  
To work with the application locally first make sure you have [python](https://www.python.org/downloads/) installed.

Then:

1. Clone the Repository

2. Set up a virtual environment using [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. Install pip Dependencies:
```Shell
pip install -r requirements.txt
```
4. Run Database [Migrations](https://flask-migrate.readthedocs.io/en/latest/)
5. Run the Flask Application locally:
```Shell
export FLASK_APP=myapp
export FLASK_ENV=development 
flask run

```
6. Verify on the Browser
Navigate to project homepage http://127.0.0.1:5000/ or http://localhost:5000

7. Run unittests
```Shell
python unittest_app.py
```
