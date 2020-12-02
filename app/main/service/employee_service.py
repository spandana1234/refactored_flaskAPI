from flask import request
from app.main import db
from app.main.model.employee import Employee


def create_emp():
    emp_name = request.json['emp_name']
    email = request.json['emaidell']
    new_emp = Employee(emp_name, email)

    db.session.add(new_emp)
    db.session.commit()

    return new_emp


def get_emps():
    return Employee.query.all()


def get_emp(id):
    return Employee.query.get(id)


def update_emp(id):
    emp = Employee.query.get(id)
    emp_name = request.json['emp_name']
    email = request.json['email']
    emp.emp_name = emp_name
    emp.email = email
    db.session.commit()
    return emp


def delete_emp(id):
    emp = Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return emp

