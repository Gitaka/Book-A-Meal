import random
import string
from flask_restful import Resource
from flask import request,jsonify

class Register(Resource):

	users = [
		             {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		             {"id":1,"email":"janedoe@gmail.com","password":"LZ8Y","token":"BLPA1FTM73","access":"1"},
		             {"id":2,"email":"johndoe@gmail.com","password":"AM5N","token":"C0G1Q5GZ81","access":"1"}
		]

	def __init__(self):
		pass

	def post(self):
		user = request.get_json(force=True)
		#all subsequent users registered on the application have a default access level of 1
		#generate a password and token for authentication
		user['id'] = ''.join(random.choice(string.digits) for x in range(1))
		user['access'] = user['access']
		user['password'] = user['password']
		user['token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
		self.users.append(user)

		message = {
		        'status':201,
		        'error':'False',
		        'message':'User successfully added' 
		}
		resp = jsonify(message)
		resp.status_code = 201
		return resp



