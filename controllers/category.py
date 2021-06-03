from flask_restful import Resource, reqparse

from config.config import mydb

class category(Resource):
    def get(self):
        data = []
        mysql_cursor = mydb.cursor()
        select_statement = "SELECT category_id,name FROM sql5416726.category"
        mysql_cursor.execute(select_statement)
        for category_id, name, in mysql_cursor.fetchall() :
            data.append({"category_id":category_id,"name":name})
        mysql_cursor.close()
        return {"data":data}