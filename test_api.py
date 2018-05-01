import os
import unittest
import json
from run import app
from app.resources.meals import Meals
from app.resources.orders import Orders
from app.resources.register import Register
from flask import request,jsonify


class ApiEndPointsTest(unittest.TestCase):
	def setUp(self):
		self.meals = Meals.meals
		self.meals.append({'id':'8','name':'Expresso','ingredients':'coffee','meal':'breakfast'})
		self.meals.append({'id':'9','name':'Mukimo','ingredients':'Maize','meal':'Lunch'})

		self.orders = Orders.orders
		self.orders.append({'id':'2',"user":'1',"description":"Rice beed","cost":'450'})

		self.users = Register.users
		self.users.append({
			"access": "0",
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM",
            "email": "JamesKinyua@gmail.com",
            "id": "0",
            "password": "password",
            "token": "BO8C1G7VGY"

        })
		
		self.users.append({
			"access": "1",
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjUxOTQsIm5iZiI6MTUyNTEyNTE5NCwianRpIjoiYmY3NGFmZmEtZjhiZS00Nzk3LTgyNWQtZDFhZjkyMmQ4ODI4IiwiZXhwIjoxNTI1MTI2MDk0LCJpZGVudGl0eSI6eyJlbWFpbCI6Ik1lbGlzc2FMZWFoQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzcyIsImFjY2VzcyI6IjAiLCJpZCI6IjUiLCJ0b2tlbiI6IjJKWDdJRDFKTzMifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.gBrCy1dc_GCAp5sxqZpazdzI2VkvXWQSu5RGx7noEnA",
            "email": "MelissaLeah@gmail.com",
            "id": "5",
            "password": "pass",
            "token": "2JX7ID1JO3"
			})

		self.app = app.test_client()


	def test_base_route(self):
		response = self.app.get('/')
		self.assertEquals(response.status_code,200)

	def test_add_to_menu(self):
		response = self.app.post('/api/v1/menu',
			       data= json.dumps({'name':'Fruit Salad','cost':'350','meal':'lunch'}),
			       headers= {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM'
			       })
		self.assertEquals(response.status_code,200)

	def test_get_menu(self):
		response = self.app.get('/api/v1/menu',
			       headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjUxOTQsIm5iZiI6MTUyNTEyNTE5NCwianRpIjoiYmY3NGFmZmEtZjhiZS00Nzk3LTgyNWQtZDFhZjkyMmQ4ODI4IiwiZXhwIjoxNTI1MTI2MDk0LCJpZGVudGl0eSI6eyJlbWFpbCI6Ik1lbGlzc2FMZWFoQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzcyIsImFjY2VzcyI6IjAiLCJpZCI6IjUiLCJ0b2tlbiI6IjJKWDdJRDFKTzMifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.gBrCy1dc_GCAp5sxqZpazdzI2VkvXWQSu5RGx7noEnA'
			       })
		self.assertEquals(response.status_code,200)

	def test_get_all_meals(self):
		response = self.app.get('/api/v1/meals',
			       headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM'
			       })
		self.assertEquals(response.status_code,200)

	def test_add_meal(self):
		data = {
		    'name':'Ugali',
		    'ingredients':'Maize flour',
		    'meal':'lunch'
		}
		response =  self.app.post('/api/v1/meals',
			        data = json.dumps(data),
			        headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM'			        
			        })
		self.assertEquals(response.status_code,200)

	def test_updating_meal(self):
		data = {
		    'name':'Omena',
		    'ingredients':'fish',
		    'meal':'lunch'
		}

		response = self.app.put('/api/v1/meals/8',
			       data = json.dumps(data),
			       headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM'
			       })
	
		self.assertEquals(response.status_code,200)

	def test_deleting_meal(self):
		response = self.app.delete('/api/v1/meals/8',
			       headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM'
			})
		self.assertEquals(response.status_code,200)

	def test_get_all_orders(self):
		response = self.app.get('/api/v1/orders',
			        headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjUxMjQxOTIsIm5iZiI6MTUyNTEyNDE5MiwianRpIjoiZmI1NTY2YjYtOGY2YS00ODhjLWE3NjktYTIwMzMzMzZkZTBmIiwiZXhwIjoxNTI1MTI1MDkyLCJpZGVudGl0eSI6eyJlbWFpbCI6IkphbWVzS2lueXVhQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicGFzc3dvcmQiLCJhY2Nlc3MiOiIwIiwiaWQiOiIwIiwidG9rZW4iOiJCTzhDMUc3VkdZIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.6DJ7w3Df8nhUV3NSs6bCkk0xK1-LcrhCcj_mVNBXDSM'
			        })
		self.assertEquals(response.status_code,200)

	def test_add_orders(self):
		data = {
		    "user":"2",
		    "description":"Ugali",
		    "cost":"450"
		}
		response = self.app.post('/api/v1/orders',
			       data = json.dumps(data),
			       headers={'token':'MDVXYGZXBO'})
		self.assertEquals(response.status_code,200)

	def test_updating_order(self):
		data = {
		    'user':'2',
		    'description':'Omena',
		    'cost':'450'
		}

		response = self.app.put('/api/v1/orders/2',
			       data = json.dumps(data),headers={'token':'MDVXYGZXBO'})
	
		self.assertEquals(response.status_code,200)


	def test_login(self):
		data = {
		      "email":"JamesKinyua@gmail.com",
		      "password":"password"
		}
		response = self.app.post('/api/v1/auth/login',data = json.dumps(data))
		self.assertEquals(response.status_code,201)

	def test_add_user(self):
		data = {
		    "email":"JamesKinyua@gmail.com",
		    "password":"password",
		    "access":"0"
		}
		response = self.app.post('/api/v1/auth/signup',
			       data = json.dumps(data))
		self.assertEquals(response.status_code,201)
    
   


if __name__ == '__main__':
	unittest.main()


