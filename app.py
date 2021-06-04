from flask import Flask,request
from flask_cors import cross_origin

from controllers.user import getUser
from controllers.user import createUser
from controllers.login import doLogin
from controllers.category import getCategories
from controllers.method import getMethods
from controllers.method import createMethod

app = Flask(__name__)

@app.route("/login",methods=['POST'])
@cross_origin()
def login():
    return doLogin()

@app.route("/user",methods=['POST','GET'])
@cross_origin()
def user():
  if request.method == 'POST':
    return createUser()
  else:
    return getUser()

@app.route("/category",methods=['GET'])
@cross_origin()
def category():
  return getCategories()

@app.route("/method",methods=['POST','GET'])
@cross_origin()
def method():
  if request.method == 'POST':
    return createMethod()
  else:
    return getMethods()


if __name__ == "__main__":
        app. run(debug=False,port=int("5000"),host='0.0.0.0') #app.run(debug=False)