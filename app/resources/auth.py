from flask_restful import Resource
from flask import request,jsonify
from app.resources.register import Register
from flask_jwt_extended import (create_access_token,
	create_refresh_token, jwt_required,jwt_refresh_token_required,
	get_jwt_identity,get_raw_jwt)

class Auth(Resource):
	#list containing users,Admin user has an access level of 0 and users have 1
	users = Register.users

	# users = [
	# 	        {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
	# 	        {"id":1,"email":"janedoe@gmail.com","password":"LZ8Y","token":"BLPA1FTM73","access":"1"},
	# 	        {"id":2,"email":"johndoe@gmail.com","password":"AM5N","token":"C0G1Q5GZ81","access":"1"}
	# 	]


	def __init__(self):
		pass


	def post(self):
		#get user data, we check for the token in the request headers
		loginDetails = request.get_json(force=True)
		for user in self.users:
			if user['email'] == loginDetails['email'] and user['password'] == loginDetails['password']:
				access_token = create_access_token(identity = user)
				#refresh_token = create_refresh_token(identity = user)
				user['access_token'] = access_token
				#user['refresh_token'] = refresh_token
				message = {
				         'message':'User Logged in',
				         'access_token': access_token,
				         #'refresh_token': refresh_token
				}
				resp = jsonify(self.users)
				resp.status_code = 201
				return resp


		else:
			message = {
			         'status':404,
                     'message':'User found',
                     'Error':'User not found'
			}
			resp = jsonify(message)
			resp.status_code = 404
			return resp






		






