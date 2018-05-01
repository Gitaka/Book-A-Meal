import random
import string
from flask_restful import Resource
from flask import request,jsonify,abort
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)
from app.resources.register import Register

class Orders(Resource):
	users = Register.users
	orders = [
		               {'id':0,"user":'1',"description":"Rice beed","cost":'450'},

		]

	def __init__(self):
		#list to hold caterer id and token
		self.caterer = [
		                {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		]

	@jwt_required
	def get(self):

		current_user = get_jwt_identity()
		#authenticate the user
		for cater in self.users:
			if cater['id'] == current_user['id'] and current_user['access'] == "0":
				#show admin the order routes
				return  jsonify(self.orders)

		message = {
		         'status':401,
		         'message':'Unauthorized access',
		         'Error':'User not found'
		}
		auth_resp = jsonify(message)
		auth_resp.status_code = 401		
		return auth_resp


	def post(self):
		order = request.get_json(force=True)
		order['id'] = ''.join(random.choice(string.digits) for x in range(1))
		self.orders.append(order)

		resp = jsonify(self.orders)
		resp.status_code = 200
		return resp

	def put(self,orderId):
		#check if the order exists
		for order in self.orders:
			if order['id'] == orderId:
				#update the order,using the json data received from request
				data = request.get_json(force=True)
				order['cost'] = data['cost']
				order['description'] = data['description']
				order['user'] = data['user']
				resp = jsonify(self.orders)
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


