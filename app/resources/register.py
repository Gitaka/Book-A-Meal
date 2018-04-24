from flask_restful import Resource
from flask import request,jsonify

class Register(Resource):
	def __init__(self):

		#list containing users,Admin user has an access level of 0 and users have 1
		self.user = [{"id":0,"token":"aaaaa","access":"0"},{"id":1,"token":"sssss","access":"1"},{"id":2,"token":"ddddd","access":"1"}]

	def post(self):
		user = request.get_json(force=True)
		self.user.append(user)
		return jsonify(self.user)


