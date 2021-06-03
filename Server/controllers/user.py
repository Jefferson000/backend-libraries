from flask_restful import Resource, reqparse

from config.config import mydb

#example to commit variables us-east-1
user_post_args = reqparse.RequestParser()
user_post_args.add_argument("email",type=str,help="the email is needed", required=True)
user_post_args.add_argument("password",type=str,help="the password is needed", required=True)
user_post_args.add_argument("name",type=str,help="the name is needed", required=True)

class user(Resource):
    def get(self):
        data = []
        mysql_cursor = mydb.cursor()
        select_statement = "SELECT user_id,name,email FROM sql5416726.account"
        mysql_cursor.execute(select_statement)
        for user_id, name,email in mysql_cursor.fetchall() :
            data.append({"user_id":user_id,"name":name,"email":email})
        mysql_cursor.close()
        return {"data":data}

    def post(self):
        args = user_post_args.parse_args()
        mysql_cursor = mydb.cursor()
        select_statement = """INSERT INTO sql5416726.account(name,email,password) VALUES('{}','{}','{}');""".format(args["name"],args["email"],args["password"])
        print(select_statement)
        try:
            mysql_cursor.execute(select_statement)
        except:
            return 'El email ya está registrado'
        mysql_cursor.close()
        mysql_cursor = mydb.cursor()
        select_statement = """SELECT user_id,name,email FROM sql5416726.account WHERE email='{}'""".format(args["email"])
        mysql_cursor.execute(select_statement)
        user_info = {}
        for user_id, name,email in mysql_cursor.fetchall() :
            user_info["user_id"]=user_id
            user_info["name"]=name
            user_info["email"]=email
        mysql_cursor.close()
        mydb.commit()
        return user_info,201
