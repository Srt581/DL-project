# import QtGUI as QtGUI
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSizePolicy, QListWidgetItem, QFileDialog
import os
import sys
from mainUI import Ui_Form
import datetime
# from recognise_character import recognise_char
from poweroffThread import PoweroffPiThread


user = "user"
passw = "pass"

class MyMainWindow(QMainWindow):
    def __init__(self, args, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_37.setText("DeepFake Face Detection")
        self.ui.pushButton.clicked.connect(self.test)
        self.ui.pushButton_13.clicked.connect(self.loginclicked)
        self.ui.pushButton_31.clicked.connect(self.backtomain)
        self.ui.pushButton_32.clicked.connect(self.checkradiobutton)
        # self.ui.pushButton_33.clicked.connect(self.clearall)
        self.ui.pushButton_35.clicked.connect(self.home)
        # self.ui.label_5.setPixmap(QtGui.QPixmap("h_02_.jpg"))
        # self.opacity_effect = QGraphicsOpacityEffect()
        # self.opacity_effect.setOpacity(0.5)
        # self.opacity_effect1 = QGraphicsOpacityEffect()
        # self.opacity_effect1.setOpacity(0.5)
        # self.ui.label_4.setGraphicsEffect(self.opacity_effect)
        # self.ui.label_5.setGraphicsEffect(self.opacity_effect1)
        self.PoweroffPiThread = PoweroffPiThread()
        self.PoweroffPiThread.signal_rx.connect(self.pinDataEvent)
        QThread.start(self.PoweroffPiThread)

    def home(self):
        self.ui.lineEdit_9.clear()
        self.ui.label_38.clear()
        # self.ui.lineEdit_5.clear()
        # self.ui.stackedWidget.setCurrentIndex(1)

    def clearall(self):
        self.ui.lineEdit_9.clear()
        self.ui.label_38.clear()
        self.ui.label_39.clear()

    def checkradiobutton(self):
        print(self.filename)
        self.ui.label_39.setText("Computing.....")
        self.PoweroffPiThread.signal_tx.emit(self.filename)
        # recognise_char(self.filename)
        # self.ui.lineEdit_9.clear()
        # self.ui.textEdit.clear()
        # self.messageBox("image encypted and file saved")

    def pinDataEvent(self, Rxdata):
        print('event test')
        print(Rxdata)
        self.ui.label_39.clear()
        self.ui.label_38.setText(Rxdata)
        print("stacked widget: ")

    def messageBox(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("student")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        print(retval)

    def backtomain(self):
        filename = QFileDialog.getOpenFileName()
        print(filename[0])
        self.filename = filename[0]
        self.ui.lineEdit_9.setText(self.filename)

    def test(self):
        print("clicked")
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.stackedWidget.setCurrentIndex(1)

    def loginclicked(self):
        print("clicked")
        username = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_5.text()
        print(username)
        print(password)
        if username == user and password == passw:
            self.ui.stackedWidget.setCurrentIndex(2)
        else:
            self.messageBox("user does not exists")
            self.ui.stackedWidget.setCurrentIndex(0)

def main():
    '''
    Main app is run here
    :return:None
    '''
    app = QApplication(sys.argv)
    argv2 = app.arguments()
    ex = MyMainWindow(argv2)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
