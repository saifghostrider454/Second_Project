# ------------------------------------------------Import--------------------------------------------------

import mysql.connector

# ------------------------------------------------Connect_to_database-------------------------------------

try:
    db = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='saif@12345',
                                 database='banking')

    cursor = db.cursor(buffered=True)
except Exception as error:
    print(error)
else:
    print(f"                         **Successfully Connected to Database**")

# ------------------------------------------------Query--------------------------------------------------

CREATE_EMPLOYEE_TABLE = """CREATE TABLE employees 
                            (
                            emp_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            first_name VARCHAR(50) NOT NULL,
                            last_name VARCHAR(50) NOT NULL,
                            salary INTEGER NOT NULL
                            )
                            """

INSERT_INTO_EMPLOYEES = "INSERT INTO employees (first_name, last_name, salary) VALUES (%s, %s, %s)"

SELECT_ALL_EMPLOYEE = "SELECT * FROM employees"

UPDATE_EMPLOYEES_SALARY = "UPDATE employees SET salary = %s WHERE emp_id = %s"


# ------------------------------------------------Function--------------------------------------------------

def execute_query(query: str):
    try:
        cursor.execute(query)
        db.commit()
    except Exception as errors:
        print(f"Execution Failed: [{errors}]")
    else:
        print("Successfully Executed")


def insert_many_query(query: str, list_of_data: list):
    try:
        cursor.executemany(query, list_of_data)
        db.commit()
    except Exception as errors:
        print(f"Execution Failed: [{errors}]")
    else:
        print("Successfully Inserted")


def grab_all(query: str):
    try:
        cursor.execute(query)
        all_employees = cursor.fetchall()
        for employee in all_employees:
            print(f"""
                     ___________________________________   
                        Employee Id:    {employee[0]}
                        First Name:     {employee[1]}
                        Last Name:      {employee[2]}
                        Salary:         {employee[3]} Rs
                     ___________________________________  

                    """)
    except Exception as errors:
        print(f"Execution Failed: [{errors}]")


def fill_emp_details():
    ask_first_name = input("Enter Employee's First Name: ").title()
    ask_last_name = input("Enter Employee's Last Name: ").title()
    ask_salary = input("Enter Employee's Salary: ")

    insert_many_query(INSERT_INTO_EMPLOYEES, [(ask_first_name, ask_last_name, ask_salary)])


def update_emp_salary():
    ask_emp_id = input("Enter Employee's ID: ")
    ask_salary = input("Enter Employee's Salary: ")
    try:
        cursor.execute(UPDATE_EMPLOYEES_SALARY, (ask_salary, ask_emp_id))
        db.commit()
    except Exception as errors:
        print(f"Execution Failed: [{errors}]")
    else:
        print("Successfully Executed")


# ----------------------------------------------------------------------------------------------------------

# execute_query(CREATE_EMPLOYEE_TABLE)

# fill_emp_details()
grab_all(SELECT_ALL_EMPLOYEE)
# update_emp_salary()
