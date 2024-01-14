from sql_connection import get_sql_connection


def get_all_products(connection):
    """
    Pass 'sql connection' as a parameter.
    Store all the products from a products table and return as a list.
    """
    response = []

    # Querying Data Using Connector
    cursor = connection.cursor()

    query = (
        "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
        "FROM grocery_store.products INNER JOIN grocery_store.uom on products.uom_id=uom.uom_id"
    )

    cursor.execute(query)

    for product_id, name, uom_id, price_per_unit, uom_name in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "uom_id": uom_id,
                "price_per_unit": price_per_unit,
                "uom_name": uom_name,
            }
        )

    cursor.close()

    return response


def insert_new_product(connection, product):
    """
    Pass 'sql connection' and product detail dictionary as the parameters.
    Insert the product into the products table.
    """

    # Querying Data Using Connector
    cursor = connection.cursor()

    query = f"INSERT INTO grocery_store.products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"

    data = (product["product_name"], product["uom_id"], product["price_per_unit"])

    cursor.execute(query, data)

    connection.commit()

    """
    In database systems, a transaction is a sequence of one or more SQL statements that are executed as a single unit of work. 
    The concept of a transaction ensures that either all the operations within the transaction are successfully executed, or none of them are. 
    The connection.commit() method is used to commit the current transaction and make the changes made during that transaction permanent.

    In the provided code, after executing the INSERT statement using cursor.execute(query, data), the changes are not immediately applied to the database. 
    Instead, they are held in a temporary state until you explicitly commit the changes using the connection.commit() method.
    """

    return cursor.lastrowid


def delete_product(connection, product_id):
    """
    Pass 'sql connection' and the product_id as the parameters.
    Delete the product from the products table.
    """

    # Querying Data Using Connector
    cursor = connection.cursor()

    quary = "DELETE FROM grocery_store.products where product_id=" + str(product_id)

    cursor.execute(quary)

    connection.commit()


def edit_product(connection, product):
    """
    Pass 'sql connection' and product detail dictionary as the parameters.
    Edit the product from the products table.
    """

    # Querying Data Using Connector
    cursor = connection.cursor()

    query = (
        "UPDATE grocery_store.products "
        "SET name = %s, uom_id = %s, price_per_unit = %s "
        "WHERE product_id = %s"
    )

    data = (
        product["name"],
        product["uom_id"],
        product["price_per_unit"],
        product["product_id"],
    )

    cursor.execute(query, data)

    connection.commit()

    return product["product_id"]


if __name__ == "__main__":
    connection = get_sql_connection()

    # product = {
    #     "product_name": "coca cola",
    #     "uom_id": "3",
    #     "price_per_unit": "200",
    # }

    # all_products = get_all_products(connection)
    # print(all_products)

    # last_row_id = insert_new_product(connection, product)
    # print(last_row_id)

    # delete_product(connection, 17)

    # product_id = edit_product(connection, product)
    # print(product_id)

    # TODO: Set the requirements.txt file -  pip install -r requirements.txt
    # TODO: Implement edit scenario
