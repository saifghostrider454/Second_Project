# ------------------------------------------------Import--------------------------------------------------

import mysql.connector

# ------------------------------------------------Connect_to_database-------------------------------------

try:
    db = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='saif@12345',
                                 database='demo_schema')

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

INSERT_INTO_DEP_ID = "INSERT INTO employees (dep_id) VALUES (%s)"


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


def grab(query: str):
    try:
        cursor.execute(query)
        all_employees = cursor.fetchall()
        for employee in all_employees:
            print(f"""
                     ___________________________________   
                        Employee Id:    {employee[0]}
                        First Name:     {employee[1]}
                        Last Name:      {employee[2]}
                        Salary:         {employee[3]} $
                     ___________________________________  
                    
                    """)
    except Exception as errors:
        print(f"Execution Failed: [{errors}]")


# ------------------------------------------------Execution--------------------------------------------------

data = [('Saif', 'Ansari', 5000),
        ('Kaif', 'Ansari', 6000),
        ('Josef', 'jwish', 6900)]

grab(SELECT_ALL_EMPLOYEE)
