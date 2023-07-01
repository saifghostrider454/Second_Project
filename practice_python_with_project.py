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

CREATE_TABLE = """
                CREATE TABLE users (
                    id INT UNSIGNED,
                    name VARCHAR(100),
                    email VARCHAR(150),
                    password VARCHAR(100),
                    contact VARCHAR(10),
                    address TEXT,
                    dob DATE,
                    gender ENUM("M", "F", "O"),
                    status BOOLEAN
                    )
                """

INSERT_ALL_VALUE = ""


# ------------------------------------------------Function--------------------------------------------------


def execute_query(query: str) -> None:
    try:
        cursor.execute(query)
        db.commit()
    except Exception as error:
        print(f"Execution Error [{error}]")
    else:
        print("Execution Successfully")


def fetching_all():
    try:
        cursor.execute("SELECT * FROM users")
        all_users = cursor.fetchall()
        for user in all_users:
            print(user)
    except Exception as error:
        print(f"Execution Error [{error}]")


# ------------------------------------------------Execution--------------------------------------------------

fetching_all()
