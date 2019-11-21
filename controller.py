from producer_consumer.producer.appconfig import app,db
from producer_consumer.producer.model import Employee
from flask import request
import json
'''********************************FOR EMPLOYEE INFO************************************************'''
@app.route("/",methods=["GET"])
def get_employees():
    emps = Employee.query.all() # list of objects in format [<Employee 1>, <Employee 2>]
    reqj = request.get_json() # Even in get request json is accepted
    print(reqj)
    employees = []
    for emp in emps:
        emp.__dict__.pop("_sa_instance_state")
        emp.__dict__.pop("is_active")
        print(emp.__dict__)
        employees.append(emp.__dict__) # imp to put __dict__ as <employee 1> is non serializable
    print(type(json.dumps(employees))) # string of list
    print(json.dumps(employees)) # list converted to string
    return json.dumps(employees) #serializing

'''********************************FOR EMPLOYEE SAVE************************************************'''
@app.route("/",methods=["POST"])
def save_employee():
    reqjson= request.get_emp()
    e1 = Employee(name=reqjson["name"],
                  salary=reqjson["salary"],
                  city=reqjson["city"])
    db.session.add(e1)
    db.session.commit()
    return {"message":" Employee record saved successfully"}

'''********************************FOR EMPLOYEE UPDATE************************************************'''
@app.route("/",methods=["PUT"])
def edit_employee():
    reqjson= request.get_json()
    e1 = Employee.query.filter_by(id=reqjson["id"]).first()
    e1.name=reqjson["name"]
    e1.city=reqjson["city"]
    e1.salary=reqjson["salary"]
    db.session.add(e1)
    db.session.commit()
    return {"message":" Employee record Updated successfully"}
'''********************************FOR EMPLOYEE DELETE************************************************'''
@app.route("/",methods=["DELETE"])
def delete_employee():
    reqjson= request.get_json()
    e1 = Employee.query.filter_by(id=reqjson["id"]).first()
    db.session.delete(e1)
    db.session.commit()
    return {"message":" Employee record Deleted successfully"}
