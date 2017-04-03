import os
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *




def onSave():
    msgBox = QMessageBox()
    msgBox.setWindowTitle("OnSave")
    msgBox.setText("btnSave was clicked.")
    msgBox.exec()


def onCancel():
    msgBox = QMessageBox()
    msgBox.setWindowTitle("OnCancel")
    msgBox.setText("btnCancel was clicked.")
    msgBox.exec()

def testPyQT():
    app = QApplication(sys.argv)
    win =  QMainWindow()
    win.setWindowTitle("Simple Form Example")
    mainWidget = QWidget(win)
    win.setCentralWidget(mainWidget)
    win.resize(500, 500)
    layout = QFormLayout()
    mainWidget.setLayout(layout)
    #title
    lblTitle = QLabel("Simple Form")
    layout.addRow(lblTitle, QLabel())
    #name
    lblName = QLabel("Name: ")
    editName = QLineEdit()
    layout.addRow(lblName, editName)
    #age
    lblAge = QLabel("Age: ")
    editAge = QLineEdit()
    layout.addRow(lblAge, editAge)
    #wage
    lblWage = QLabel("Wage: ")
    editWage = QLineEdit()
    layout.addRow(lblWage, editWage)
    #buttons
    btnSave = QPushButton("Save")
    btnCancel = QPushButton("Cancel")
    layout.addRow(btnSave, btnCancel)
    btnSave.clicked.connect(onSave)
    btnCancel.clicked.connect(onCancel)
    win.show()

    sys.exit(app.exec_())

    #sys.exit(app.exec())


class MyMainWindow(QMainWindow):
    # mainWidget = QWidget()
    # layout = QFormLayout()
    # lblTitle = QLabel()
    # lblName = QLabel()
    # lblAge = QLabel()
    # lblWage = QLabel()
    # editName = QLineEdit()
    # editAge = QLineEdit()
    # editWage = QLineEdit()
    # btnSave = QPushButton()
    # btnCancel = QPushButton()


    def configureWindow(self):
        self.resize(500, 500)
        self.setWindowTitle("Simple Form Example")
        self.addWidgets()
        self.registerEvents()

    def addWidgets(self):
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.layout = QFormLayout()
        self.mainWidget.setLayout(self.layout)
        #title
        self.lblTitle = QLabel("Simple Worker Form")
        self.layout.addRow(self.lblTitle , QLabel())
        #name
        self.lblName = QLabel("Name: ")
        self.editName = QLineEdit()
        self.layout.addRow(self.lblName, self.editName)
        #age
        self.lblAge = QLabel("Age: ")
        self.editAge = QLineEdit()
        self.layout.addRow(self.lblAge, self.editAge)
        #wage
        self.lblWage = QLabel("Wage: ")
        self.editWage = QLineEdit()
        self.layout.addRow(self.lblWage, self.editWage)
        #buttons
        self.btnSave = QPushButton("Save")
        self.btnCancel = QPushButton("Cancel")
        self.layout.addRow(self.btnSave, self.btnCancel)

    def registerEvents(self):
        self.btnSave.clicked.connect(self.onSave)
        self.btnCancel.clicked.connect(self.onCancel)
    def onSave(self):
        name = self.editName.text()
        age = self.editAge.text()
        wage = self.editWage.text()
        msgBox = QMessageBox()
        msgBox.setWindowTitle("On Save")
        msgBox.setText("name = {}\nage = {}\nwage = {}".format(name, age, wage))
        msgBox.exec()
    def onCancel(self):
        self.editName.clear()
        self.editAge.clear()
        self.editWage.clear()

def testMyMainWindow():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.configureWindow()
    window.show()
    sys.exit(app.exec())


def main():
    testMyMainWindow()



if __name__ == "__main__":
    main()
