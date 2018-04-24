import os
import unittest
from app import app

class ApiEndPointsTest(unittest.TestCase):

	def test_base_route(self):
		self.test_app = app.test_client()
		response = self.test_app.get('/')
		self.assertEquals(response.status_code,200)

	def test_addToMenu(self):
		self.test_app = app.test_client()
		response = self.test_app.post('/api/v1/menu',data={'id':8,'name':'Fruit Salad'})
		self.assertEquals(response.status_code,200)

	def test_getMenu(self):
		self.test_app = app.test_client()
		response = self.test_app.get('/api/v1/menu')
		self.assertEquals(response.status_code,200)

	def test_getAllMeals(self):
		self.test_app = app.test_client()
		response = self.test_app.get('/api/v1/meals')
		self.assertEquals(response.status_code,200)

	def test_addMeal(self):
		self.test_app = app.test_client()
		response =  self.test_app.post('/api/v1/meals',data={'id':8,'name':'Ugali','ingredients':'maize flour','meal':'lunch'})
		self.assertEquals(response.status_code,200)

	def test_updatingMeal(self):
		self.test_app = app.test_client()
		response = self.test_app.put('/api/v1/meals/2',data={"id":"2","name":"Omena","ingredients":"fish","meal":"lunch"})
		self.assertEquals(response.status_code,200)

	def test_deletingMeal(self):
		self.test_app = app.test_client()
		response = self.test_app.delete('/api/v1/meals/2')
		self.assertEquals(response.status_code,200)

	def test_getAllOrders(self):
		self.test_app = app.test_client()
		response = self.test_app.get('/api/v1/orders')
		self.assertEquals(response.status_code,200)

	def test_addOrders(self):
		self.test_app = app.test_client()
		response = self.test_app.post('/api/v1/orders',data={"id":3,"user":"2","description":"tilapia","cost":"450"})
		self.assertEquals(response.status_code,200)

	def login(self,token):
		#user login with a token sent to request header
		self.test_app = app.test_client()
		return self.test_app.post('/api/v1/auth/login',data={"username":"gitaka","password":"pass"},headers={'token':'aaaaa'})

	def test_login(self):
		res = self.login('token')
		self.assertEquals(res,{"message":"User logged in successfully"})

	def test_addUser(self):
		self.test_app = app.test_client()
		response = self.test_app.post('/api/v1/auth/signup',data={"id":0,"token":"vvvvv","access":"1"})
		self.assertEquals(response.status_code,200)
    
   


if __name__ == '__main__':
	unittest.main()


