from flask import Flask, request, jsonify
from flask_cors import CORS
from random_username.generate import generate_username

app = Flask(__name__)
CORS(app)

users = { 
   'users_list':
   [
      { 
         'id' : 'abc789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello world! Travis did it.'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')

        if not (search_username or search_job):
            return users 

        if search_username and search_job:
            filtered = filter(lambda c: c['name'] == search_username and c['job'] == search_job, users['users_list'])
            return { 'users_list': filtered }
        elif search_username:
            filtered = find_users_by_name(search_username)
            return { 'users_list': filtered }
        elif search_job:
            filtered = filter(lambda c: c['job'] == search_job, users['users_list'])
            return { 'users_list': filtered }
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = generate_username()[0]
        users['users_list'].append(userToAdd)
        return userToAdd, 201

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
                return ({})
    elif request.method == 'DELETE':
        if id in map(lambda a: a['id'], users['users_list']): # does the id exist in the lis
            users['users_list'] = list(filter(lambda a: a['id'] != id, users['users_list']))
            return jsonify(success=True), 204
        return jsonify(success=False), 404
    return users

def find_users_by_name(name):
    filtered = filter(lambda c: c['name'] == name, users['users_list'])
    return list(filtered)
