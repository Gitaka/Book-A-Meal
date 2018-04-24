from flask_restful import Resource
from flask import request,jsonify

class Menu(Resource):
	def __init__(self):
		self.authUsers = [{'id':1,"token":"eeeee"},{'id':2,"token":"rrrrr"}]
		self.caterer = [{'id':0,'token':"aaaaa"}]
		self.menu = [{'id':0,'name':'Expresso','ingredients':'coffee','meal':'breakfast'},
		{'id':1,'name':'Githeri','ingredients':'maize,beans','meal':'lunch'},
		{'id':2,'name':'Tilapia','ingredients':'fish','meal':'lunch'},
		{'id':3,'name':'Ugali','ingredients':'maize','meal':'supper',},
		{'id':4,'name':'Rice beef','ingredients':'rice,beef','meal':'lunch'},
		{'id':5,'name':'Chapati beef','ingredients':'chapati beef','meal':'supper'},
		{'id':6,'name':'Mukimo','ingredients':'maize,potatoe','meal':'supper'}
	]		

	def get(self):
		#extract the authenticated userId from querystring
		uId = int(request.args['id'])
		#check if user is authenticated
		for user in self.authUsers:
			if user['id'] == uId:
				return jsonify(self.menu)

		return {"Error":"User not authenticated"}



	def post(self):
		data = request.get_json(force=True)
		#authenticate if the token supplied in the header corresponds to the caterers token
		#extract the token and assign it to a variable
		token = request.headers['token']
		for cater in self.caterer:
			if cater['token'] == token:
				#add menu to menu list
				self.menu.append(data)

				return jsonify(self.menu)
		return {"Error":"Not authorised"}
