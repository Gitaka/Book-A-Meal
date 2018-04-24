from app import app
from flask_restful import Api
from app.resources.meals import Meals
from app.resources.menu import Menu
from app.resources.orders import Orders
from app.resources.auth import Auth
from app.resources.register import Register

api = Api(app)
api.add_resource(Meals,'/api/v1/meals','/api/v1/meals','/api/v1/meals/<string:mealId>','/api/v1/meals/<string:mealId>')
api.add_resource(Menu,'/api/v1/menu','/api/v1/menu')
api.add_resource(Orders,'/api/v1/orders','/api/v1/orders','/api/v1/orders/<string:orderId>')
api.add_resource(Register,'/api/v1/auth/signup')
api.add_resource(Auth,'/api/v1/auth/login')

@app.route("/")
def hello():

    return "Book-A-Meal application"
 
if __name__ == "__main__":
    app.run()