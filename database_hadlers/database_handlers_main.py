import sqlite3


sql_conn = None
cursor = None


# create functions part
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
    cr_table_products_for_menu = """CREATE TABLE IF NOT EXISTS prod_menu(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    date_operation DATE,
                                                                    date_menu DATE,
                                                                    name_product TEXT,
                                                                    unit TEXT,
                                                                    quantity_storage REAL,
                                                                    quantity_for_menu REAL,
                                                                    date_time_op TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"""

    cursor.execute(cr_table_product_query)
    cursor.execute(cr_table_products_query)
    cursor.execute(cr_table_products_for_menu)

    sql_conn.commit()

#get_db_connection()


# insert functions part
def insert_product_data(data):
    cursor.execute("""INSERT INTO product ( source_name, source_number, dest_name, dest_number,
                                            date_operation, name_product, unit, quantity,
                                            price, total, type_operation, manufacturer,
                                            production_date, expiration_date, number_document,
                                            date_document, number_directive, date_directive) 
                                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", data)
    sql_conn.commit()


def insert_or_update_products(data_insert):
    data_insert = list(data_insert)
    name_product = data_insert[0].split(' ')
    if len(name_product) >= 4:
        name_product = (f'{name_product[0]} {name_product[1]} {name_product[2]} {name_product[3]}%',)
    elif len(name_product) >= 3:
        name_product = (f'{name_product[0]} {name_product[1]} {name_product[2]}%',)
    elif len(name_product) >= 2:
        name_product = (f'{name_product[0]} {name_product[1]}%',)
    else:
        name_product = (f'{name_product[0]}%',)

    data_select = cursor.execute("""SELECT * FROM all_products WHERE name_product LIKE ?""", name_product).fetchone()

    try:
        data_select = data_select
    except:
        data_select = None

    if data_select:
        if data_insert[3] == 'Убуток':
            data_insert[2] = -abs(float(data_insert[2]))
        sum_quantity = float(data_insert[2]) + data_select[3]
        update_data = (sum_quantity, name_product[0])
        cursor.execute("""UPDATE all_products SET quantity = ? WHERE name_product LIKE ?""", update_data)
    else:
        cursor.execute("""INSERT INTO all_products (name_product, unit, quantity) VALUES (?,?,?)""", data_insert[:3])
    sql_conn.commit()


def update_products_dec(data):
    data[3] = -abs(float(data[3]))
    name_product = (data[0],)
    data_select = cursor.execute("""SELECT * FROM all_products WHERE name_product LIKE ?""", name_product).fetchone()
    sum_quantity = round(float(data[3]) + data_select[3], 3)
    update_data = (sum_quantity, name_product[0])
    # print(update_data)
    cursor.execute("""UPDATE all_products SET quantity = ? WHERE name_product LIKE ?""", update_data)
    sql_conn.commit()


def insert_prod_menu(data):
    cursor.executemany("""INSERT INTO prod_menu(date_operation, date_menu, name_product, unit, quantity_storage, quantity_for_menu) VALUES (?,?,?,?,?,?)""", data)
    sql_conn.commit()


# select functions part
def parse_db_all_products():
    '''
    parsing main file
    '''
    cursor.execute("""SELECT * FROM all_products ORDER BY name_product""")
    records = cursor.fetchall()
    return records


def select_menu_data(dates):
    date_1 = f'{dates[0][6:]}-{dates[0][3:5]}-{dates[0][0:2]}'
    date_2 = f'{dates[1][6:]}-{dates[1][3:5]}-{dates[1][0:2]}'
    dates = date_1, date_2
    # dates - tuple with two dates, Example: ('24.11.2024', '25.11.2024')
    # dates get from two fields GUI
    cursor.execute("""SELECT * FROM prod_menu WHERE date_time_op BETWEEN ? AND ?""", dates) # date_menu
    data_menu_select = cursor.fetchall()
    return data_menu_select



# select_()