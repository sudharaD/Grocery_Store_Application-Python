from sql_connection import get_sql_connection


def get_uoms(connection):
    """
    Pass 'sql connection' as a parameter.
    Store all the uoms from a uom table and return as a list.
    """

    response = []

    # Querying Data Using Connector
    cursor = connection.cursor()

    query = "SELECT * FROM grocery_store.uom"

    cursor.execute(query)

    for uom_id, uom_name in cursor:
        response.append({"uom_id": uom_id, "uom_name": uom_name})

    cursor.close()

    return response


if __name__ == "__main__":
    connection = get_sql_connection()
