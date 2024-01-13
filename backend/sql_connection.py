import mysql.connector

__cnx = None

"""
In Python, when you define a variable inside a function, it is considered local to that function by default. If you want to modify a global variable from within a function, you need to use the global keyword to indicate that the variable being referenced is the global one, not a local one.

In the provided code, the __cnx variable is declared outside the function get_sql_connection, making it a global variable. Inside the function, the global __cnx statement is used to indicate that the variable being referenced is the global one, not a local variable created within the function.

Without the global keyword, if you tried to modify the variable __cnx inside the function, Python would create a new local variable with the same name, and any modifications would be made to the local variable, not the global one. This is why the global keyword is necessary in this context.

In summary, the global keyword is used to indicate that a variable is a global variable and should be modified at the global scope, not as a local variable within a function. It ensures that changes made to the variable inside the function affect the global variable, not a local one with the same name.
"""


def get_sql_connection():
    global __cnx

    if __cnx == None:
        # Create the connection with sql server
        __cnx = mysql.connector.connect(
            user="root", password="password", host="127.0.0.1", database="grocery_store"
        )

    return __cnx
