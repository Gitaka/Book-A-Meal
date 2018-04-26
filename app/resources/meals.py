from flask_restful import Resource
from flask import request,jsonify,abort


class Meals(Resource):
	def __init__(self):

		self.caterer = [
		                {"id":0,"email":"gitakaMuchai@BookAMeal.com","password":"KY2W","token":"MDVXYGZXBO","access":"0"},
		]
		self.meals = [
		              {'id':0,'name':'Expresso','ingredients':'coffee','meal':'breakfast'},
		              {'id':1,'name':'Githeri','ingredients':'maize,beans','meal':'lunch'},
		              {'id':2,'name':'Tilapia','ingredients':'fish','meal':'lunch'},
		              {'id':3,'name':'Ugali','ingredients':'maize','meal':'supper',},
		              {'id':4,'name':'Rice beef','ingredients':'rice,beef','meal':'lunch'},
		              {'id':5,'name':'Chapati beef','ingredients':'chapati beef','meal':'supper'},
		              {'id':6,'name':'Mukimo','ingredients':'maize,potatoe','meal':'supper'}

		]

	
	def get(self):
		#extract the token from the request header
		if 'token' in request.headers:
			token = request.headers['token']
		else:
			abort(404)
		#authenticate the token
		for cater in self.caterer:
			if cater['token'] == token:
				#show admin the order routes
				return  jsonify(self.meals)
		return {"Error":"UnAuthorized access"}		
		

	def post(self):
		if'token' in request.headers:
			token = request.headers['token']
		else:
			abort(404)
		for cater in self.caterer:
			if cater['token'] == token:
				meals = self.meals
				meals.append(request.get_json(force=True))
				return jsonify(meals)
		return {"Error":"UnAuthorized access"}	


	def put(self,mealId):
		#if no token header exists give a 404 error
		if 'token' in request.headers:
			token = request.headers['token']
		else:
			abort(404)

		for cater in self.caterer:
			if cater['token'] == token:
				#get the mealid
				mealId = int(mealId)
				data = request.get_json(force=True)

				#look the meal item to update on the list
				for meal in self.meals:
					if meal['id'] == mealId:
						meal['meal'] == data['meal']
						meal['ingredients'] = data['ingredients']
						meal['name'] = data['name']
				return jsonify(self.meals)

		return {"Error":'UnAuthorized access'}





	def delete(self,mealId):
		#if no token header exists give a 404 error
		if 'token' in request.headers:
			token = request.headers['token']
		else:
			return "404 not found"

		for cater in self.caterer:
			if cater['token'] == token:
				mealId = int(mealId)
				for meal in self.meals:
					if meal['id'] == mealId:
						del self.meals[meal['id']]
				return jsonify(self.meals)

		return {"Error":'UnAuthorized access'}




		
		
			
				
		


