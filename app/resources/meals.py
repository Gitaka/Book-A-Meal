import random,string
from flask_restful import Resource
from flask import request,jsonify,abort
from flask_jwt_extended import (create_access_token,
	create_refresh_token, jwt_required,jwt_refresh_token_required,
	get_jwt_identity,get_raw_jwt)
from app.resources.register import Register

class Meals(Resource):
	users = Register.users


	meals = []
	# meals = [

	# 	{'id':0,'name':'Expresso','ingredients':'coffee','meal':'breakfast'},
	# 	{'id':1,'name':'Githeri','ingredients':'maize,beans','meal':'lunch'},
	# 	{'id':2,'name':'Tilapia','ingredients':'fish','meal':'lunch'},
	# 	{'id':3,'name':'Ugali','ingredients':'maize','meal':'supper',},
	# 	{'id':4,'name':'Rice beef','ingredients':'rice,beef','meal':'lunch'},
	# 	{'id':5,'name':'Chapati beef','ingredients':'chapati beef','meal':'supper'},
	# 	{'id':6,'name':'Mukimo','ingredients':'maize,potatoe','meal':'supper'}

	# 	]

	def __init__(self):


		self.caterer = [
		                {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		]

	@jwt_required
	def get(self):
		current_user = get_jwt_identity()
		for user in self.users:
			if user['id'] == current_user['id'] and current_user['access'] == '0':
				resp = jsonify(self.meals)
				resp.status_code = 200
				return resp
		else:
			message = {
			         'status':401,
			         'message':'Unauthorized access',
			         'error':'User not found'
			}
			resp = jsonify(message)
			resp.status_code = 400
			return resp

	@jwt_required
	def post(self):
		current_user = get_jwt_identity()

		for cater in self.users:
			if cater['id'] == current_user['id'] and current_user['access'] == '0':
				meal = request.get_json(force=True)
				meal["id"] = ''.join(random.choice(string.digits) for x in range(1))
				self.meals.append(meal)
				resp = jsonify(self.meals)
				resp.status_code = 201
				return resp 

		message = {
		         'status':401,
		         'message':'Unauthorized access',
		         'Error':'User not found'
		}
		auth_resp = jsonify(message)
		auth_resp.status_code = 401	
		return auth_resp

	@jwt_required
	def put(self,mealId):
		current_user = get_jwt_identity()

		for cater in self.users:
			if cater['id'] == current_user['id'] and current_user['access'] == '0':
				#get data from request
				data = request.get_json(force=True)

				#look the meal item to update on the list
				for meal in self.meals:
					if meal['id'] == mealId:
						meal['meal'] = data['meal']
						meal['ingredients'] = data['ingredients']
						meal['name'] = data['name']
						resp = jsonify(self.meals)
						resp.status_code = 200
						return resp
				else:
					message = {
					         'status':404,
					         'message':'Not found',
					         'Error':'Meal item not found'
					}
					resp = jsonify(message)
					resp.status_code = 404

					return resp


		message = {
		         'status':401,
		         'message':'Unauthorized access',
		         'Error':'User not found'
		}
		auth_resp = jsonify(message)
		auth_resp.status_code = 401	
		return auth_resp

	@jwt_required
	def delete(self,mealId):
		current_user = get_jwt_identity()

		for cater in self.users:
			if cater['id'] == current_user['id'] and current_user['access'] == '0':
				for meal in self.meals:
					#return jsonify(meal['id'])
					 if meal['id'] == mealId:
					 	self.meals.remove(meal)
					 	resp = jsonify(self.meals)
					 	resp.status_code = 200
					 	return resp
					 	
				else:
					message = {
					         'status':404,
					         'message':'Not found',
					         'Error':'Meal item not found'
					}
					resp = jsonify(message)
					resp.status_code = 404
					return resp



		message = {
		         'status':401,
		         'message':'Unauthorized access',
		         'Error':'User not found'
		}
		auth_resp = jsonify(message)
		auth_resp.status_code = 401	
		return auth_resp




		
		
			
				
		


