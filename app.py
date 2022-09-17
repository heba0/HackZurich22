from flask import Flask,request, jsonify
# import flask
from flask_cors import CORS
# import ast
# from linkedin_configure import auth, headers
# import requests


# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,POST,PATCH,DELETE,OPTIONS')
    return response


# ----------------------------------------------------------------------------#
# Routes.
# ----------------------------------------------------------------------------#

@app.route('/api/v0', methods=['GET'])
def home():
    return 'HACKZURICH 2022!'
#
# def get_credentials():
#
#
# def user_info(headers):
#     '''
#     Get user information from Linkedin
#     '''
#     response = requests.get('https://api.linkedin.com/v2/me', headers = headers)
#     resp = flask.Response("Foo bar baz")
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     user_info = response.json()
#     credentials = 'credentials.json'
#     access_token = auth(credentials) # Authenticate the API
#     headers = headers(access_token) # Make the headers to attach to the API call.
#     user_info = user_info(headers) # Get user info
#
#
# # orgaisations data
# @app.route('/api/v0/linkedin', methods=['GET'])
# def user_info(headers):
#     '''
#     Get user information from Linkedin
#     '''
#     response = requests.get('https://api.linkedin.com/v2/me', headers = headers)
#     user_info = response.json()
#     return user_info
#
# @app.route('/api/v0', methods=['POST'])
# def search_organisations():
#     return "", 201
#

# ----------------------------------------------------------------------------#
# Error Handling.
# ----------------------------------------------------------------------------#

@app.errorhandler(400)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'bad request'
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }, 405)


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable'
    }), 422


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal Server Error'
    }, 500)


# allows running with Flask or Python
if __name__ == "__main__":
    app.run(host='localhost', port=8080)