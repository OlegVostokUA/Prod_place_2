# pip install pyinstaller
# pyinstaller -F -w -i "C:\Users\User\PycharmProjects\ProdPlace\MainApp\main.ico" MainApp.py

import sys
from datetime import datetime

from PyQt5.QtGui import QFont # QIcon, QPixmap,
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from database_hadlers.database_handlers_main import get_db_connection, insert_product_data, insert_or_update_products


get_db_connection(path_to_db_file='database/prod_database.db')


class LossProfitTab(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(LossProfitTab, self).__init__()
        self.label_date = QLabel(self)
        self.label_date.setText('Введіть дату операції:')
        self.input_date = QDateEdit(self)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(datetime.today())
        self.label_type_oper = QLabel(self)
        self.label_type_oper.setText('Введіть тип операції:')
        self.input_type_oper = QComboBox(self)
        self.input_type_oper.addItems(['Прибуток', 'Убуток'])
        self.label_source_name = QLabel(self)
        self.label_source_name.setText('Назва постачальника (назва в/ч)')
        self.input_source_name = QLineEdit()
        self.label_source_number = QLabel(self)
        self.label_source_number.setText('Номер постачальника (номер в/ч)')
        self.input_source_number = QLineEdit()
        self.label_destination_name = QLabel(self)
        self.label_destination_name.setText('Назва отримувача (назва в/ч)')
        self.input_destination_name = QLineEdit()
        self.label_destination_number = QLabel(self)
        self.label_destination_number.setText('Номер отримувача (номер в/ч)')
        self.input_destination_number = QLineEdit()
        self.label_product_name = QLabel(self)
        self.label_product_name.setText('Назва продукції')
        self.input_product_name = QLineEdit()
        self.label_unit = QLabel(self)
        self.label_unit.setText('  Одиниця виміру  ')
        self.input_unit = QComboBox(self)
        self.input_unit.addItems(['кг', 'шт', 'к-т', 'л', 'др'])
        self.label_product_quantity = QLabel(self)
        self.label_product_quantity.setText('Кількість')
        self.input_product_quantity = QLineEdit()
        self.label_product_price = QLabel(self)
        self.label_product_price.setText('Ціна')
        self.input_product_price = QLineEdit()
        self.label_product_total = QLabel(self)
        self.label_product_total.setText('Сума')
        self.input_product_total = QLineEdit()
        self.label_manufacturer = QLabel(self)
        self.label_manufacturer.setText('Виробник')
        self.input_manufacturer = QLineEdit()
        self.label_production_date = QLabel(self)
        self.label_production_date.setText('    Дата виробництва    ')
        self.input_production_date = QDateEdit(self)
        self.input_production_date.setCalendarPopup(True)
        self.input_production_date.setDate(datetime.today())
        self.label_expiration_date = QLabel(self)
        self.label_expiration_date.setText('Кінцева дата споживання')
        self.input_expiration_date = QDateEdit(self)
        self.input_expiration_date.setCalendarPopup(True)
        self.input_expiration_date.setDate(datetime.today())
        self.label_number_document = QLabel(self)
        self.label_number_document.setText('Номер первинного документу (накладна / акт)')
        self.input_number_document = QLineEdit()
        self.label_date_document = QLabel(self)
        self.label_date_document.setText(' Дата первинного документу ')
        self.input_date_document = QDateEdit(self)
        self.input_date_document.setCalendarPopup(True)
        self.input_date_document.setDate(datetime.today())
        self.label_number_directive = QLabel(self)
        self.label_number_directive.setText('Номер документу(розпорядження / договір)')
        self.input_number_directive = QLineEdit()
        self.label_date_directive = QLabel(self)
        self.label_date_directive.setText('     Дата документу     ')
        self.input_date_directive = QDateEdit(self)
        self.input_date_directive.setCalendarPopup(True)
        self.input_date_directive.setDate(datetime.today())
        # create buttons
        self.save_to_db = QPushButton('   Зберегти у Базу Даних')
        self.save_to_db.setIcon(QtGui.QIcon('icons/database.png'))
        self.save_to_db.clicked.connect(self.push_to_database)

        # layout box
        main_layout = QVBoxLayout(self)
        # 1 row
        input_form_layout = QHBoxLayout(self)
        input_form_layout.addWidget(self.label_date)
        input_form_layout.addWidget(self.input_date)
        input_form_layout.addSpacing(200)
        input_form_layout.addWidget(self.label_type_oper)
        input_form_layout.addWidget(self.input_type_oper)
        # 2 row
        input_source_dest_layout = QHBoxLayout(self)
        input_source_name_layout = QVBoxLayout(self)
        input_source_name_layout.addWidget(self.label_source_name)
        input_source_name_layout.addWidget(self.input_source_name)
        input_source_num_layout = QVBoxLayout(self)
        input_source_num_layout.addWidget(self.label_source_number)
        input_source_num_layout.addWidget(self.input_source_number)
        input_dest_name_layout = QVBoxLayout(self)
        input_dest_name_layout.addWidget(self.label_destination_name)
        input_dest_name_layout.addWidget(self.input_destination_name)
        input_dest_num_layout = QVBoxLayout(self)
        input_dest_num_layout.addWidget(self.label_destination_number)
        input_dest_num_layout.addWidget(self.input_destination_number)
        input_source_dest_layout.addLayout(input_source_name_layout)
        input_source_dest_layout.addLayout(input_source_num_layout)
        input_source_dest_layout.addLayout(input_dest_name_layout)
        input_source_dest_layout.addLayout(input_dest_num_layout)
        # 3 row
        input_product = QHBoxLayout(self)
        input_name_product = QVBoxLayout(self)
        input_name_product.addWidget(self.label_product_name)
        input_name_product.addWidget(self.input_product_name)
        input_product_unit_pr_ttl = QHBoxLayout(self)
        input_unit_layout = QVBoxLayout(self)
        input_unit_layout.addWidget(self.label_unit)
        input_unit_layout.addWidget(self.input_unit)
        input_quantity_layout = QVBoxLayout(self)
        input_quantity_layout.addWidget(self.label_product_quantity)
        input_quantity_layout.addWidget(self.input_product_quantity)
        input_price_layout = QVBoxLayout(self)
        input_price_layout.addWidget(self.label_product_price)
        input_price_layout.addWidget(self.input_product_price)
        input_total_layout = QVBoxLayout(self)
        input_total_layout.addWidget(self.label_product_total)
        input_total_layout.addWidget(self.input_product_total)
        input_product_unit_pr_ttl.addLayout(input_unit_layout)
        input_product_unit_pr_ttl.addLayout(input_quantity_layout)
        input_product_unit_pr_ttl.addLayout(input_price_layout)
        input_product_unit_pr_ttl.addLayout(input_total_layout)
        input_product.addLayout(input_name_product)
        input_product.addLayout(input_product_unit_pr_ttl)
        # 4 row
        input_mf_date_layout = QHBoxLayout(self)
        input_mf_layout = QVBoxLayout(self)
        input_mf_layout.addWidget(self.label_manufacturer)
        input_mf_layout.addWidget(self.input_manufacturer)
        input_pr_date_layout = QVBoxLayout(self)
        input_pr_date_layout.addWidget(self.label_production_date)
        input_pr_date_layout.addWidget(self.input_production_date)
        input_exp_date_layout = QVBoxLayout(self)
        input_exp_date_layout.addWidget(self.label_expiration_date)
        input_exp_date_layout.addWidget(self.input_expiration_date)
        input_mf_date_layout.addLayout(input_mf_layout)
        input_mf_date_layout.addLayout(input_pr_date_layout)
        input_mf_date_layout.addLayout(input_exp_date_layout)
        # 5 row
        input_documents = QHBoxLayout(self)
        input_num_doc_layout = QVBoxLayout(self)
        input_num_doc_layout.addWidget(self.label_number_document)
        input_num_doc_layout.addWidget(self.input_number_document)
        input_date_doc_layout = QVBoxLayout(self)
        input_date_doc_layout.addWidget(self.label_date_document)
        input_date_doc_layout.addWidget(self.input_date_document)
        input_num_dir_layout = QVBoxLayout(self)
        input_num_dir_layout.addWidget(self.label_number_directive)
        input_num_dir_layout.addWidget(self.input_number_directive)
        input_date_dir_layout = QVBoxLayout(self)
        input_date_dir_layout.addWidget(self.label_date_directive)
        input_date_dir_layout.addWidget(self.input_date_directive)
        input_documents.addLayout(input_num_doc_layout)
        input_documents.addLayout(input_date_doc_layout)
        input_documents.addLayout(input_num_dir_layout)
        input_documents.addLayout(input_date_dir_layout)
        # button
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.save_to_db)

        main_layout.addLayout(input_form_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(input_source_dest_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(input_product)
        main_layout.addSpacing(15)
        main_layout.addLayout(input_mf_date_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(input_documents)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def push_to_database(self):
        data_tuple = (self.input_source_name.text(),
                      self.input_source_number.text(),
                      self.input_destination_name.text(),
                      self.input_destination_number.text(),
                      self.input_date.text(),
                      self.input_product_name.text(),
                      self.input_unit.currentText(),
                      self.input_product_quantity.text(),
                      self.input_product_price.text(),
                      self.input_product_total.text(),
                      self.input_type_oper.currentText(),
                      self.input_manufacturer.text(),
                      self.input_production_date.text(),
                      self.input_expiration_date.text(),
                      self.input_number_document.text(),
                      self.input_date_document.text(),
                      self.input_number_directive.text(),
                      self.input_date_directive.text())
        #print(data_tuple)
        insert_product_data(data_tuple)
        data_tuple_2 = (self.input_product_name.text(),
                        self.input_unit.currentText(),
                        self.input_product_quantity.text(),
                        self.input_type_oper.currentText())
        insert_or_update_products(data_tuple_2)


class MainWindow(QMainWindow):
    """
    MAIN window Class
    """
    def __init__(self):
        super().__init__() # initialization widgets and properties Parent class "QDialog"
        # in here we set widgets and set properties
        self.setWindowTitle('eBook')
        self.setWindowIcon(QtGui.QIcon('icons/main.png'))
        #self.setWindowTitle("My App") # title of app
        self.resize(1150, 1000) # set size window
        font = QFont("Times New Roman", 14, 75, True) # set font window
        # add widgets
        self.main_widget = QTabWidget()
        self.setCentralWidget(self.main_widget)
        self.main_widget.addTab(LossProfitTab(), "Прихід / Розхід")



### Final App Block ###
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    # app.setStyle('Oxygen') # 'Breeze'
    dlgMain = MainWindow() # build object of class "DlgMain" and set here in variable "dlgMain"
    dlgMain.show() # show function
    sys.exit(app.exec_())  # loop app in "sys.exit" func for check logs.

