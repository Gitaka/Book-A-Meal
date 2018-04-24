from flask_restful import Resource
from flask import request,jsonify

class Auth(Resource):
	def __init__(self):

		#list containing users,Admin user has an access level of 0 and users have 1
		self.users = [{"id":0,"token":"aaaaa","access":"0"},{"id":1,"token":"sssss","access":"1"},{"id":2,"token":"ddddd","access":"1"}]

	def post(self):
		#get user data, we check for the token in the request headers
		if 'token' in request.headers:
			token = request.headers['token']
		else:
			return{"Error":"404 not found"}
		#search for the user in our list using the token
		for user in self.users:
			if user['token'] == token:
				#user is authenticated,return that users details
				loginDetails = request.get_json(force=True)
				return {"message":"User logged in successfully"}

		return {"message":"Login failed."}




