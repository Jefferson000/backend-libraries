from flask.globals import request
from flask_restful import Resource, reqparse
from flask_cors import cross_origin
from config.config import mydb
import json

#Controlador para obtener un usuario del sistema, no hay parámetros requeridos
def getUser():
    data = []
    mysql_cursor = mydb.cursor()
    select_statement = "SELECT user_id,name,email FROM sql5418609.account"
    mysql_cursor.execute(select_statement)
    for user_id, name,email in mysql_cursor.fetchall() :
        data.append({"user_id":user_id,"name":name,"email":email})
    mysql_cursor.close()
    return {'data':data},200

#Controlador para crear usuarios e insertarlos en la base de datos, parámetros requeridos:
# name,email,password
def createUser():
    params = json.loads(request.data.decode('utf-8'))
    mysql_cursor = mydb.cursor()
    select_statement = """INSERT INTO sql5418609.account(name,email,password) VALUES('{}','{}','{}');""".format(params["name"],params["email"],params["password"])
    print(select_statement)
    try:
        mysql_cursor.execute(select_statement)
    except:
        return {'error':'El email ya está registrado'},400
    mysql_cursor.close()
    mysql_cursor = mydb.cursor()
    select_statement = """SELECT user_id,name,email FROM sql5418609.account WHERE email='{}'""".format(params["email"])
    mysql_cursor.execute(select_statement)
    user_info = {}
    for user_id, name,email in mysql_cursor.fetchall() :
        user_info["user_id"]=user_id
        user_info["name"]=name
        user_info["email"]=email
    mysql_cursor.close()
    mydb.commit()
    return {"data":user_info},201
