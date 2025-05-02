# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(363, 491)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 12, 56, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 70, 53, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(12, 128, 61, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(12, 186, 109, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(12, 243, 46, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(12, 301, 26, 16))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(12, 359, 71, 16))
        self.cmbCat = QComboBox(Dialog)
        self.cmbCat.setObjectName(u"cmbCat")
        self.cmbCat.setGeometry(QRect(11, 40, 331, 24))
        self.cmbPla = QComboBox(Dialog)
        self.cmbPla.setObjectName(u"cmbPla")
        self.cmbPla.setGeometry(QRect(11, 267, 331, 24))
        self.txtNam = QLineEdit(Dialog)
        self.txtNam.setObjectName(u"txtNam")
        self.txtNam.setGeometry(QRect(11, 99, 331, 21))
        self.txtFin = QLineEdit(Dialog)
        self.txtFin.setObjectName(u"txtFin")
        self.txtFin.setGeometry(QRect(11, 155, 331, 21))
        self.txtCont = QLineEdit(Dialog)
        self.txtCont.setObjectName(u"txtCont")
        self.txtCont.setGeometry(QRect(11, 211, 331, 21))
        self.txtDesc = QLineEdit(Dialog)
        self.txtDesc.setObjectName(u"txtDesc")
        self.txtDesc.setGeometry(QRect(11, 384, 331, 21))
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(11, 326, 331, 23))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 420, 351, 61))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnRem = QPushButton(self.widget)
        self.btnRem.setObjectName(u"btnRem")

        self.horizontalLayout.addWidget(self.btnRem)

        self.btnAdd = QPushButton(self.widget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0448\u0435\u0434\u0448\u0438\u0439", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043d\u0435\u043c", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None))
        self.btnRem.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

