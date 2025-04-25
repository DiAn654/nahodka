import sys
import os
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from PySide6 import QtCore
from mainwindow import Ui_MainWindow
#from edit_dialog import Ui_Dialog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session



dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///db.db", echo=True)

        self.load_fin()
        self.load_pla()
        self.load_cat()
        self.load_loit()

        self.ui.cmbCat.currentIndexChanged.connect(self.load_loit)


    def load_loit(self):
        cat_data = self.ui.cmbCat.currentData()
        if cat_data:
            cat_id = self.ui.cmbCat.currentData().id
        else:
            cat_id = 0
        
        self.ui.lstItems.clear()

        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM lost_items
            WHERE (:cid = 0 OR cat_id = :cid)
            """

            rows = s.execute(text(query), {"cid": cat_id})
            for r in rows:
                cat_n = self.categ[r.cat_id].name 
                plac_n = self.plac[r.pla_id].place
                fin_n = self.fin[r.fin_id].full_name

                self.ui.lstItems.addItem(f"{cat_n} {r.item_name} {r.found_date} {plac_n} {fin_n}") #добавляем на лист наши данные
    



    def load_cat(self):
        self.categ = {}

        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM categ
            """

            rows = s.execute(text(query))
            for r in rows:
                self.categ[r.id] = r 
        self.ui.cmbCat.addItem("-")
        for r in self.categ.values():
            self.ui.cmbCat.addItem(r.name, r)


    def load_fin(self):
        self.fin = {}
        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM finders
            """

            rows = s.execute(text(query))
            for r in rows:
                self.fin[r.id] = r


    def load_pla(self):
        self.plac = {}

        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM places
            """

            rows = s.execute(text(query))
            for r in rows:
                self.plac[r.id] = r 




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())