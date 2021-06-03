from flask import Flask
from flask_restful import Api

from controllers.user import user
from controllers.login import login
from controllers.category import category
from controllers.method import method

app = Flask(__name__)

api = Api(app)

api.add_resource(user,"/user")
api.add_resource(login,"/login")
api.add_resource(category,"/category")
api.add_resource(method,"/method")

if __name__ == "__main__":
        app. run(debug=False,port=int("5000"),host='0.0.0.0') #app.run(debug=False)