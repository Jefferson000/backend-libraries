from flask_restful import Resource, reqparse
from flask_cors import cross_origin
from config.config import mydb

def getCategories():
    data = []
    mysql_cursor = mydb.cursor()
    select_statement = "SELECT category_id,name FROM sql5418609.category"
    mysql_cursor.execute(select_statement)
    for category_id, name, in mysql_cursor.fetchall() :
        data.append({"category_id":category_id,"name":name})
    mysql_cursor.close()
    return {"data":data}