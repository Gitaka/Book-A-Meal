import random
import string
from flask_restful import Resource
from flask import request,jsonify

class Register(Resource):
	def __init__(self):

		#list containing users,Admin user has an access level of 0 and users have 1
		self.users = [
		             {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		             {"id":1,"email":"janedoe@gmail.com","password":"LZ8Y","token":"BLPA1FTM73","access":"1"},
		             {"id":2,"email":"johndoe@gmail.com","password":"AM5N","token":"C0G1Q5GZ81","access":"1"}
		]

	def post(self):
		user = request.get_json(force=True)
		#all subsequent users registered on the application have a default access level of 1
		#generate a password and token for authentication
		user['id'] = ''.join(random.choice(string.digits) for x in range(1))
		user['access'] = '1'
		user['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
		user['token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
		self.users.append(user)
        
        #open a file users.txt that stores user data and append(register) the new user
		file = open("users.txt","a")
		file.write(str(user))
		file.write('\n')
		file.close()

		return jsonify(user)


