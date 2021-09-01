from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from database.models import setup_db, db, Owner, Breed, Cat, Adoption_Interview 

def create_app():
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  

  """ uncomment at the first time running the app """
    #db_drop_and_create_all()


  @app.route('/', methods=['GET'])
  def healthy(): return jsonify({"status":"healthy"}),200

  #TODO: Endpoints will include at least…
    # Two GET requests
    # One POST request
    # One PATCH request
    # One DELETE request

  @app.route('/Adopt', methods=['GET'])
  def view_all_pets():
    return jsonify({'pets': [Cat.details() for cat in Cat.query.all()]}), 200

  @app.route('/Interview', methods=['GET'])
  def view_upcoming_interviews():
    return jsonify({})#({'pets': [Adoption_Interview.details() for interview in Adoption_Interview.query.all()]}), 200

  @app.route('/Cat', methods=['POST'])
  def post_Cat_information():
    return jsonify({''}), 201

  @app.route('/Cat', methods=['PATCH'])
  def view_cat_information():
    return jsonify({''}), 204 # 200 (OK) or 204 (No Content)
  
  @app.route('/Cat', methods=['DELETE'])
  def delete_Cat_information():
    return jsonify({''}), 200


  @app.errorhandler(500)
  def server_error(error):
      return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
      }), 500

  return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8080, debug=True)