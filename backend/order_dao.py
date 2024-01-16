from sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection, order):
    """
    Pass 'sql connection' and order as the parameters.
    Insert the order into the order and order details table.
    """
    cursor = connection.cursor()

    order_query = "INSERT INTO grocery_store.orders (customer_name, total, datetime) VALUES (%s, %s, %s)"
    order_data = (order["customer_name"], order["grand_total"], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_quary = "INSERT INTO grocery_store.order_details (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)"

    order_details_data = []

    for order_details_record in order["order_details"]:
        order_details_data.append(
            [
                order_id,
                int(order_details_record["product_id"]),
                float(order_details_record["quantity"]),
                float(order_details_record["total_price"]),
            ]
        )

    cursor.executemany(order_details_quary, order_details_data)

    connection.commit()

    cursor.close()

    return order_id


def get_all_orders(connection):
    """
    Pass 'sql connection' as a parameter.
    Get all the orders from a order table and return as a list.
    """
    cursor = connection.cursor()

    query = "SELECT * from orders"

    cursor.execute(query)

    response = []

    for order_id, customer_name, total, datetime in cursor:
        response.append(
            {
                "order_id": order_id,
                "customer_name": customer_name,
                "total": total,
                "datetime": datetime,
            }
        )

    return response


if __name__ == "__main__":
    connection = get_sql_connection()
    # print(
    #     insert_order(
    #         connection,
    #         {
    #             "customer_name": "khali",
    #             "grand_total": 400,
    #             "order_details": [
    #                 {"product_id": 1, "quantity": 2, "total_price": 50},
    #                 {"product_id": 1, "quantity": 2, "total_price": 50},
    #                 {"product_id": 1, "quantity": 2, "total_price": 50},
    #             ],
    #         },
    #     )
    # )
    print(get_all_orders(connection))
