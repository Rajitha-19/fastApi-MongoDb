from fastapi import FastAPI 
from models import employee
from pydantic import BaseModel
from mongoengine import connect
import json
app=FastAPI()
connect(db="mongoLearning",host="localhost",port=27017)
app.get("/")
def home():
    return {"message":"Hello World!"}
@app.get("/get_all_employees")
def get_all_employees():
    employees=employee.objects().to_json()
    employees_list= json.loads(employees)
    print(type(employees_list))
    return {"employees":employees_list}
