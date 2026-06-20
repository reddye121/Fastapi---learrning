from fastapi import FastAPI

app = FastAPI()

employees=[]

@app.get("/employees")
def get_all_employees():
    return employees

@app.post("/employees")
def add_employees(employee:dict):
    employees.append(employee)
    return {"message":"Successfully added",
            "emp":employee}

@app.put("/employees")
def update_employees(upd_emp:dict):
    for emp in employees:
        if emp["id"]== upd_emp["id"]:
            emp.update(upd_emp)
            return {"message":"Change is successfully updated",
                    "change":emp}
    return {"message":"employee not found"}


@app.delete("/employees/{emp_id}")
def delete_employees(emp_id:int):
    for emp in employees:
        if emp["id"]== emp_id:
            employees.remove(emp)
            return {"message":"Change is successfully updated"}




