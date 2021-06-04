from flask import Flask,request
from flask_restful import Api

from controllers.user import getUser
from controllers.user import createUser
from controllers.login import login
from controllers.category import category
from controllers.method import method
from flask_cors import cross_origin

app = Flask(__name__)

# api = Api(app)

# api.add_resource(user,"/user")
# api.add_resource(login,"/login")
# api.add_resource(category,"/category")
# api.add_resource(method,"/method")
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/login",methods=['POST','GET'])
@cross_origin()
def user():
    if request.method == 'GET':
        return getUser()
    else:
        return createUser()
        
if __name__ == "__main__":
        app. run(debug=False,port=int("5000"),host='0.0.0.0') #app.run(debug=False)