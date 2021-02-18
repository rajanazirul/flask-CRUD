#app/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
from flask import request, jsonify, abort
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

#config name refer to development, staging, testing, production
def crud_app(config_name): 

    from app.models import Userlist

    # run app based on config environment
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    #validate duplicate
    def validate(name, email):
        userlists = Userlist.get_all()
        results = []

        for userlist in userlists:
            obj = {
                'id': userlist.id,
                'name': userlist.name,
                'email': userlist.email,
                'date_created': userlist.date_created,
                'date_modified': userlist.date_modified
            }
            results.append(obj)
        i = 0
        while i<len(results):
            if name == results[i]['name'] or email == results[i]['email']:
                return True
            i = i + 1 

    #API script
    @app.route('/userlists/', methods=['POST', 'GET'])
    def userlists():
        if request.method == 'POST':
            #POST method
            name = str(request.data.get('name', ''))
            email = str(request.data.get('email', ''))
            
            if validate(name, email) != True:
                userlist = Userlist(name=name, email=email)
                userlist.save()
                response = jsonify({
                    'id': userlist.id,
                    'name': userlist.name,
                    'email': userlist.email,
                    'date_created': userlist.date_created,
                    'date_modified': userlist.date_modified
                })
                response.status_code = 201
                return response
            else:
                return {
                    "message": "user already exist"
                }, 200
        
        else:
            #GET method
            userlists = Userlist.get_all()
            results = []

            for userlist in userlists:
                obj = {
                    'id': userlist.id,
                    'name': userlist.name,
                    'email': userlist.email,
                    'date_created': userlist.date_created,
                    'date_modified': userlist.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
    
    @app.route('/userlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def userlists_edit(id, *kwargs):
        #get userlist using its ID
        userlist= Userlist.query.filter_by(id=id).first()
        if not userlist:
            abort(404)
        
        if request.method == 'DELETE':
            userlist.delete()
            return {
                "message": "user {} deleted successfully".format(userlist.id)
            }, 200

        elif request.method == 'PUT':
            
            name = str(request.data.get('name', ''))
            email = str(request.data.get('email', ''))
            if validate(name, email) != True:
                userlist.name = name
                userlist.email = email
                userlist.save()
                response = jsonify({
                    'id': userlist.id,
                    'name': userlist.name,
                    'email': userlist.email,
                    'date_created': userlist.date_created,
                    'date_modified': userlist.date_modified
                })
                response.status_code = 200
                return response
            else:
                return {
                    "message": "user already exist"
                }, 200
        else:
            response = jsonify({
                'id': userlist.id,
                'name': userlist.name,
                'email': userlist.email,
                'date_created': userlist.date_created,
                'date_modified': userlist.date_modified
            })
            response.status_code = 200
            return response
    return app


    
    
