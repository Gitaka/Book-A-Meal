import os
import unittest
from app import app

class ApiEndPointsTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()


	def test_base_route(self):
		response = self.app.get('/')
		self.assertEquals(response.status_code,200)

	def test_add_to_menu(self):
		response = self.app.post('/api/v1/menu',
			       data={'id':8,'name':'Fruit Salad'})
		self.assertEquals(response.status_code,200)

	def test_get_menu(self):
		response = self.app.get('/api/v1/menu')
		self.assertEquals(response.status_code,200)

	def test_get_all_meals(self):
		response = self.app.get('/api/v1/meals')
		self.assertEquals(response.status_code,200)

	def test_add_meal(self):
		data = {
		    'id':8,
		    'name':'Ugali',
		    'ingredients':'Maize flour',
		    'meal':'lunch'
		}
		response =  self.app.post('/api/v1/meals',
			        data = data)
		self.assertEquals(response.status_code,200)

	def test_updating_meal(self):
		data = {
		    'id':2,
		    'name':'Omena',
		    'ingredients':'fish',
		    'meal':'lunch'
		}
		response = self.app.put('/api/v1/meals/2',
			       data = data)
		self.assertEquals(response.status_code,200)

	def test_deleting_meal(self):
		response = self.app.delete('/api/v1/meals/2')
		self.assertEquals(response.status_code,200)

	def test_get_all_orders(self):
		response = self.app.get('/api/v1/orders')
		self.assertEquals(response.status_code,200)

	def test_add_orders(self):
		data = {
		    "id":3,
		    "user":"2",
		    "description":"tilapia",
		    "cost":"450"
		}
		response = self.app.post('/api/v1/orders',
			       data = data)
		self.assertEquals(response.status_code,200)



	def test_login(self):
		data = {
		      "username":"gitaka",
		      "password":"pass"
		}
		response = self.app.post('/api/v1/auth/login',data = data, headers={"token":"C0G1Q5GZ81"})
		self.assertEquals(response.status_code,200)

	def test_add_user(self):
		data = {
		    "id":0,
		    "token":"vvvvv",
		    "access":"1"
		}
		response = self.app.post('/api/v1/auth/signup',
			       data = data)
		self.assertEquals(response.status_code,200)
    
   


if __name__ == '__main__':
	unittest.main()


