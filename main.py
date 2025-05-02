import sys
import os
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from PySide6 import QtCore
from mainwindow import Ui_MainWindow
from edit_dialog import Ui_Dialog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from datetime import date, timedelta
from PySide6.QtCore import QDate

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class EditDialog(QDialog):
    
    def __init__(self, categ, plac, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.engine = create_engine("sqlite+pysqlite:///db.db", echo=True)


        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnRem.clicked.connect(self.reject)

        for r in categ.values():
            self.ui.cmbCat.addItem(r.name, r)
        for r in plac.values():
            self.ui.cmbPla.addItem(r.place, r)


    def get_d(self):
        return{
            "cat_id": self.ui.cmbCat.currentData().id,
            "pla_id": self.ui.cmbPla.currentData().id,
            "item_name": self.ui.txtNam.text()
        }




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

        self.ui.dateFromEdit.setDisplayFormat("dd.MM.yyyy")
        self.ui.dateToEdit.setDisplayFormat("dd.MM.yyyy")
        today = QDate.currentDate()
        week_ago = today.addDays(-7)

        self.ui.dateFromEdit.setDate(week_ago)
        self.ui.dateToEdit.setDate(today)
        self.ui.dateFromEdit.dateChanged.connect(self.load_loit)
        self.ui.dateToEdit.dateChanged.connect(self.load_loit)

        self.ui.cmbCat.currentIndexChanged.connect(self.load_loit)
        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)


    def on_btnAdd_click(self):
        dialog = EditDialog(self.categ, self.plac)
        r = dialog.exec()
        if r == 0:
            return

        data = dialog.get_d()
        with Session(self.engine) as s:
            query = """
            INSERT INTO lost_items(cat_id, item_name, pla_id)
            VALUES (:cat, :it, :pl)
            """

            s.execute(text(query), {
                "cat": data['cat_id'], 
                "pl": data['pla_id'],
                "it": data['item_name'],
            })
            s.commit()


    def load_loit(self):
        
        cat_data = self.ui.cmbCat.currentData()
        if cat_data:
            cat_id = self.ui.cmbCat.currentData().id
        else:
            cat_id = 0
        
        self.ui.lstItems.clear()
        date_from = self.ui.dateFromEdit.date().toPython()
        date_to = self.ui.dateToEdit.date().toPython()

        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM lost_items
            WHERE (:cid = 0 OR cat_id = :cid)
                AND date (found_date) BETWEEN date (:fdate_from) AND date (:fdate_to)
            """

            rows = s.execute(text(query), {
                "cid": cat_id,
                "fdate_from": date_from.strftime('%Y-%m-%d'),
                "fdate_to": date_to.strftime('%Y-%m-%d')
                })
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