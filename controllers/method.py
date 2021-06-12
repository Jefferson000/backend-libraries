from flask import request
from config.config import mydb
import json

def getMethods():
    data = []
    query_parms = request.query_string.decode("utf-8")
    print(query_parms)
    criteria = ''
    if(query_parms!=''and 'criteria=' in query_parms):
        criteria = request.query_string.decode("utf-8").split("=")[1]
    mysql_cursor = mydb.cursor()
    select_statement = """
        SELECT m.method_id as method_id, m.name as method_name, m.code as method_code, m.description as method_description,a.name as user_name,c.name as category_name FROM sql5418609.method as m 
        INNER JOIN sql5418609.account as a ON a.user_id = m.user_id
        INNER JOIN sql5418609.category as c ON c.category_id = m.category_id
        WHERE m.name LIKE '%{}%' OR a.name LIKE '%{}%' OR c.name LIKE '%{}%';""".format(criteria,criteria,criteria)
    mysql_cursor.execute(select_statement)
    for method_id,method_name, method_code,method_description,user_name,category_name in mysql_cursor.fetchall() :
        data.append({"method_id":method_id,"method_name":method_name,"method_code":method_code,"method_description":method_description,"user_name":user_name,"category_name":category_name})
    mysql_cursor.close()
    return {"data":data}

def createMethod():
    params = json.loads(request.data.decode('utf-8'))
    mysql_cursor = mydb.cursor()
    select_statement = """INSERT INTO sql5418609.method(name,code,description,user_id,category_id) 
    VALUES('{}','{}','{}',{},{});""".format(params["method_name"],params["method_code"],params["method_description"],params["user_id"],params["category_id"])
    print(select_statement)
    try:
        mysql_cursor.execute(select_statement)
    except:
        return {'error':'Ya existe función con ese nombre'},400
    mysql_cursor.close()
    mysql_cursor = mydb.cursor()
    select_statement = """
        SELECT m.method_id as method_id, m.name as method_name, m.code as method_code, m.description as method_description,a.name as user_name,c.name as category_name FROM sql5418609.method as m 
        INNER JOIN sql5418609.account as a ON a.user_id = m.user_id
        INNER JOIN sql5418609.category as c ON c.category_id = m.category_id WHERE m.name='{}'""".format(params["method_name"])
    mysql_cursor.execute(select_statement)
    user_info = {}
    for method_id,method_name, method_code,method_description,user_name,category_name  in mysql_cursor.fetchall() :
        user_info["method_id"]=method_id
        user_info["method_name"]=method_name
        user_info["method_code"]=method_code
        user_info["method_description"]=method_description
        user_info["user_name"]=user_name
        user_info["category_name"]=category_name
    mysql_cursor.close()
    mydb.commit()
    return user_info,201
