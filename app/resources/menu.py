from flask_restful import Resource
from flask import request,jsonify,abort

class Menu(Resource):
	def __init__(self):
		self.authUsers = [
		                  {"id":1,"email":"janedoe@gmail.com","password":"LZ8Y","token":"BLPA1FTM73","access":"1"},
		                  {"id":2,"email":"johndoe@gmail.com","password":"AM5N","token":"C0G1Q5GZ81","access":"1"}
		]
		self.caterer = [ 
		                {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		]
		self.menu = [
		              {'id':0,'name':'Expresso','cost':'300','meal':'breakfast'},
		              {'id':1,'name':'Githeri','cost':'200','meal':'lunch'},
		              {'id':2,'name':'Tilapia','cost':'450','meal':'lunch'},
		              {'id':3,'name':'Ugali','cost':'400','meal':'supper',},
		              {'id':4,'name':'Rice beef','cost':'600','meal':'lunch'},
		              {'id':5,'name':'Chapati beef','cost':'300','meal':'supper'},
		              {'id':6,'name':'Mukimo','cost':'600','meal':'supper'}
	    ]		   

	def get(self):
		#extract the user authenticated token from querystring
		if 'token' in request.headers:
			uId = request.headers['token']
		else:
			abort(404)
		#check if user is authenticated
		for user in self.authUsers:
			if user['token'] == uId:
				return jsonify(self.menu)

		return {"Error":"User not authenticated"}



	def post(self):
		data = request.get_json(force=True)
		#authenticate if the token supplied in the header corresponds to the caterers token
		#extract the token and assign it to a variable
		if 'token' in request.headers:
			token = request.headers['token']
		else:
			abort(404)
		for cater in self.caterer:
			if cater['token'] == token:
				#add menu to menu list
				self.menu.append(data)

				return jsonify(self.menu)
		return {"Error":"Not authorised"}
