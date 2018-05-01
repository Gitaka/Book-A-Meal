import random
import string
from flask_restful import Resource
from flask import request,jsonify,abort
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)
from app.resources.register import Register

class Menu(Resource):
	users = Register.users
	menu = []
	def __init__(self):
		self.authUsers = [
		                  {"id":1,"email":"janedoe@gmail.com","password":"LZ8Y","token":"BLPA1FTM73","access":"1"},
		                  {"id":2,"email":"johndoe@gmail.com","password":"AM5N","token":"C0G1Q5GZ81","access":"1"}
		]
		self.caterer = [ 
		                {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		]
		# self.menu = [
		#               {'id':0,'name':'Expresso','cost':'300','meal':'breakfast'},
		#               {'id':1,'name':'Githeri','cost':'200','meal':'lunch'},
		#               {'id':2,'name':'Tilapia','cost':'450','meal':'lunch'},
		#               {'id':3,'name':'Ugali','cost':'400','meal':'supper',},
		#               {'id':4,'name':'Rice beef','cost':'600','meal':'lunch'},
		#               {'id':5,'name':'Chapati beef','cost':'300','meal':'supper'},
		#               {'id':6,'name':'Mukimo','cost':'600','meal':'supper'}
	 #    ]		   

	@jwt_required
	def get(self):
		current_user = get_jwt_identity()

		#check if user is authenticated
		for user in self.users:
			if user['id'] == current_user['id'] and current_user['access'] == "1":
				return jsonify(self.menu)
		message = {
		         'status':401,
		         'message':'Unauthorized access',
		         'Error':'User not found'
		}
		auth_resp = jsonify(message)
		auth_resp.status_code = 401		
		return auth_resp

	@jwt_required
	def post(self):
		data = request.get_json(force=True)
		current_user = get_jwt_identity()

		for cater in self.users:
			if cater['id'] == current_user['id'] and current_user['access'] == "0":
				#add menu to menu list
				data['id'] = ''.join(random.choice(string.digits) for x in range(1))
				self.menu.append(data)
				return jsonify(self.menu)


		message = {
		         'status':401,
		         'message':'Unauthorized access',
		         'Error':'User not found'
		}
		auth_resp = jsonify(message)
		auth_resp.status_code = 401		
		return auth_resp

