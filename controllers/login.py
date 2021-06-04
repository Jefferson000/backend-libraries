from flask.wrappers import Response
from flask_restful import Resource, reqparse
from flask import Response
from flask_cors import cross_origin
from config.config import mydb
#example to commit variables us-east-1
login_post_args = reqparse.RequestParser()
login_post_args.add_argument("email",type=str,help="the email is needed", required=True)
login_post_args.add_argument("password",type=str,help="the passwordt is needed", required=True)

class login(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get(self):
        data = []
        mysql_cursor = mydb.cursor()
        sql_statement = "SELECT user_id,name,email FROM sql5416726.account"
        mysql_cursor.execute(sql_statement)
        for user_id, name,email in mysql_cursor.fetchall() :
            data.append({"user_id":user_id,"name":name,"email":email})
        mysql_cursor.close()
        
        return {"data":data}

    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def post(self):
        args = login_post_args.parse_args()
        mysql_cursor = mydb.cursor()
        sql_statement = """SELECT user_id,name,email FROM sql5416726.account WHERE email='{}' AND password='{}'""".format(args["email"],args["password"])
        print(sql_statement)
        try:
            mysql_cursor.execute(sql_statement)
        except:
            return 'Error de autentificación',404
        user_info = {}
        for user_id, name,email in mysql_cursor.fetchall():
            user_info["user_id"]=user_id
            user_info["name"]=name
            user_info["email"]=email
        if user_info =={}:
            return 'error de autentificación',404
        mysql_cursor.close()
        return user_info,201
        # return Response(headers={'Access-Control-Allow-Origin':'*'},content_type='application/json', response=str(user_info),status=200)
