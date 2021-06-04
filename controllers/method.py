from flask_restful import Resource, reqparse
from flask import request
from flask_cors import cross_origin
from config.config import mydb

#example to commit variables us-east-1
method_post_args = reqparse.RequestParser()
method_post_args.add_argument("method_name",type=str,help="the name is needed", required=True)
method_post_args.add_argument("method_code",type=str,help="the code is needed", required=True)
method_post_args.add_argument("method_description",type=str,help="the description is needed", required=True)
method_post_args.add_argument("user_id",type=str,help="the user_id is needed", required=True)
method_post_args.add_argument("category_id",type=str,help="the category_id is needed", required=True)

class method(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get(self):
        data = []
        query_parms = request.query_string.decode("utf-8")
        print(query_parms)
        criteria = ''
        if(query_parms!=''and 'criteria=' in query_parms):
            criteria = request.query_string.decode("utf-8").split("=")[1]
        mysql_cursor = mydb.cursor()
        select_statement = """
            SELECT m.method_id as method_id, m.name as method_name, m.code as method_code, m.description as method_description,a.name as user_name,c.name as category_name FROM sql5416726.method as m 
            INNER JOIN sql5416726.account as a ON a.user_id = m.user_id
            INNER JOIN sql5416726.category as c ON c.category_id = m.category_id
            WHERE m.name LIKE '%{}%' OR a.name LIKE '%{}%' OR c.name LIKE '%{}%';""".format(criteria,criteria,criteria)
        mysql_cursor.execute(select_statement)
        for method_id,method_name, method_code,method_description,user_name,category_name in mysql_cursor.fetchall() :
            data.append({"method_id":method_id,"method_name":method_name,"method_code":method_code,"method_description":method_description,"user_name":user_name,"category_name":category_name})
        mysql_cursor.close()
        return {"data":data}

    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def post(self):
        args = method_post_args.parse_args()
        mysql_cursor = mydb.cursor()
        select_statement = """INSERT INTO sql5416726.method(name,code,description,user_id,category_id) 
        VALUES('{}','{}','{}',{},{});""".format(args["method_name"],args["method_code"],args["method_description"],args["user_id"],args["category_id"])
        print(select_statement)
        try:
            mysql_cursor.execute(select_statement)
        except:
            return 'Ya existe una función con ese nombre'
        mysql_cursor.close()
        mysql_cursor = mydb.cursor()
        select_statement = """
            SELECT m.method_id as method_id, m.name as method_name, m.code as method_code, m.description as method_description,a.name as user_name,c.name as category_name FROM sql5416726.method as m 
            INNER JOIN sql5416726.account as a ON a.user_id = m.user_id
            INNER JOIN sql5416726.category as c ON c.category_id = m.category_id WHERE m.name='{}'""".format(args["method_name"])
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
