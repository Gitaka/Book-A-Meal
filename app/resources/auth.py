from flask_restful import Resource
from flask import request,jsonify

class Auth(Resource):
	def __init__(self):

		#list containing users,Admin user has an access level of 0 and users have 1
		self.users = [
		             {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		             {"id":1,"email":"janedoe@gmail.com","password":"LZ8Y","token":"BLPA1FTM73","access":"1"},
		             {"id":2,"email":"johndoe@gmail.com","password":"AM5N","token":"C0G1Q5GZ81","access":"1"}
		]

	def post(self):
		#get user data, we check for the token in the request headers
		if 'token' in request.headers:
			token = request.headers['token']
		else:
			return{"Error":"404 not found"}
		#read all the users from the text file and put them in a list
		#authenticate the sent token by searching it in the returned list above
		authUsers = []
		file = open("users.txt","r")
		for user in file:
			authUsers.append(eval(user))
		file.close()

		for thisUser in authUsers:
			if thisUser['token'] == token:
				logInDetails = request.get_json(force=True)
				return {"message":"User Logged in Successfully"}
		#return error if user not found
		return {"message":"Email or Password incorrect"}

		






