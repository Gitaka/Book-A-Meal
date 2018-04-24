from flask_restful import Resource
from flask import request,jsonify

class Orders(Resource):
	def __init__(self):
		#list to hold caterer id and token
		self.caterer = [{"id":0,"token":"aaaaa"}]

		self.orders = [{'id':0,"user":'1',"description":"Rice beed","cost":'450'},
                       {'id':2,"user":"2","description":"Chapati beef","cost":"300"}
		]

	def get(self):
		#extract the token from the request header
		token = request.headers['token']
		#authenticate the token
		for cater in self.caterer:
			if cater['token'] == token:
				#show admin the order routes
				return  jsonify(self.orders)
		return {"Error":"UnAuthorized access"}

	def post(self):
		order = request.get_json(force=True)
		self.orders.append(order)
		return jsonify(self.orders)

	def put(self,orderId):
		#check if the order exists
		orderId = int(orderId)
		for order in self.orders:
			if order['id'] == orderId:
				#update the order,using the json data received from request
				data = request.get_json(force=True)
				order['user'] = data['user']
				order['description'] = data['description']
				order['cost'] = data['cost']
			return jsonify(self.orders)

