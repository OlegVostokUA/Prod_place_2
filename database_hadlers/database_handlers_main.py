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
                                                                    expiration_date DATE,
                                                                    number_document TEXT,
                                                                    date_document DATE,
                                                                    number_directive TEXT,
                                                                    date_directive DATE)"""
    cr_table_products_query = """CREATE TABLE IF NOT EXISTS all_products(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    name_product TEXT,
                                                                    unit TEXT,
                                                                    quantity REAL)"""

    cursor.execute(cr_table_product_query)
    cursor.execute(cr_table_products_query)

    sql_conn.commit()

#get_db_connection()

def insert_product_data(data):
    cursor.execute("""INSERT INTO product ( source_name, source_number, dest_name, dest_number,
                                            date_operation, name_product, unit, quantity,
                                            price, total, type_operation, manufacturer,
                                            production_date, expiration_date, number_document,
                                            date_document, number_directive, date_directive) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   data)
    sql_conn.commit()


def insert_or_update_products(data_insert):
    name_product = data_insert[0].split(' ')
    try:
        name_product = (name_product[0] + ' ' + name_product[1],)
    except:
        name_product = (name_product[0],)
    print(name_product)
    data_select = cursor.execute("""SELECT * FROM all_products WHERE name_product LIKE ?""", name_product).fetchall()
    # print(data_select)
    try:
        data_select = data_select[0]
    except:
        data_select = None

    if data_select:
        print('yes')
    else:
        print('no')





def select_():
    data = cursor.execute("""SELECT * FROM product""").fetchall()
    print(data)

# select_()