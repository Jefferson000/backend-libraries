from flask import request
from config.config import mydb
import json 

def doLogin():
    params = json.loads(request.data.decode('utf-8'))
    mysql_cursor = mydb.cursor()
    sql_statement = """SELECT user_id,name,email FROM sql5418609.account WHERE email='{}' AND password='{}'""".format(params["email"],params["password"])
    print(sql_statement)
    try:
        mysql_cursor.execute(sql_statement)
    except:
        return {'error':'error de autentificación'},401
    user_info = {}
    for user_id, name,email in mysql_cursor.fetchall():
        user_info["user_id"]=user_id
        user_info["name"]=name
        user_info["email"]=email
    if user_info =={}:
        return {'error':'error de autentificación'},401
    mysql_cursor.close()
    return {"data":user_info},200