import sqlite3


sql_conn = None
cursor = None


def get_db_connection(path_to_db_file=None):
    """
    func for connection to database and create tables
    """
    global sql_conn, cursor

    if not path_to_db_file:
        path_to_db_file = '../database/prod_database.db'

    sql_conn = sqlite3.connect(path_to_db_file)
    cursor = sql_conn.cursor()

    cr_table_product_query = """CREATE TABLE IF NOT EXISTS product( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    source_name TEXT,
                                                                    source_number TEXT,
                                                                    dest_name TEXT,
                                                                    dest_number TEXT,
                                                                    date_operation DATE,
                                                                    name_product TEXT,
                                                                    unit TEXT,
                                                                    quantity REAL,
                                                                    price REAL,
                                                                    total REAL,
                                                                    type_operation TEXT,
                                                                    manufacturer TEXT,
                                                                    production_date DATE,
                                                                    expiration_date DATE)"""

    cursor.execute(cr_table_product_query)

    sql_conn.commit()





#get_db_connection()