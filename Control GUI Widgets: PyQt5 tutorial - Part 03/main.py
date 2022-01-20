# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 643)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/radar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(413, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 333, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("font: 48pt \"Sans Serif\";\n"
"background-color: rgb(170, 170, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_6.addLayout(self.verticalLayout, 1, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dial = QtWidgets.QDial(self.tab_2)
        self.dial.setObjectName("dial")
        self.horizontalLayout_2.addWidget(self.dial)
        spacerItem4 = QtWidgets.QSpacerItem(20, 208, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(333, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dial_2 = QtWidgets.QDial(self.tab_2)
        self.dial_2.setObjectName("dial_2")
        self.verticalLayout_2.addWidget(self.dial_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.dial_3 = QtWidgets.QDial(self.tab_2)
        self.dial_3.setObjectName("dial_3")
        self.verticalLayout_2.addWidget(self.dial_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 2, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setStyleSheet("font: 48pt \"Sans Serif\";\n"
"background-color: rgb(85, 255, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 221, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalSlider = QtWidgets.QSlider(self.tab_3)
        self.verticalSlider.setSliderPosition(24)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_5.addWidget(self.verticalSlider, 0, 0, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setStyleSheet("font: 48pt \"Sans Serif\";\n"
"background-color: rgb(0, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_3)
        self.horizontalSlider.setSliderPosition(99)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_5.addWidget(self.horizontalSlider, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 20))
        self.menubar.setObjectName("menubar")
        self.menuPyshine = QtWidgets.QMenu(self.menubar)
        self.menuPyshine.setObjectName("menuPyshine")
        self.menuSubmenu = QtWidgets.QMenu(self.menuPyshine)
        self.menuSubmenu.setObjectName("menuSubmenu")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionitem1 = QtWidgets.QAction(MainWindow)
        self.actionitem1.setObjectName("actionitem1")
        self.actionitem_2 = QtWidgets.QAction(MainWindow)
        self.actionitem_2.setObjectName("actionitem_2")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.menuSubmenu.addAction(self.actionitem1)
        self.menuSubmenu.addAction(self.actionitem_2)
        self.menuPyshine.addAction(self.actionNew)
        self.menuPyshine.addAction(self.actionExit)
        self.menuPyshine.addAction(self.menuSubmenu.menuAction())
        self.menuView.addAction(self.actionMaximize)
        self.menuView.addAction(self.actionNormal)
        self.menubar.addAction(self.menuPyshine.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionMaximize.triggered.connect(MainWindow.showMaximized)
        self.actionNormal.triggered.connect(MainWindow.showNormal)
        self.lineEdit.textEdited['QString'].connect(self.label_3.setText)
        self.verticalSlider.valueChanged['int'].connect(self.label_3.setNum)
        self.horizontalSlider.valueChanged['int'].connect(self.label_3.setNum)
        self.lineEdit_2.textEdited['QString'].connect(self.label_2.setText)
        self.dial.valueChanged['int'].connect(self.label_2.setNum)
        self.dial_3.valueChanged['int'].connect(self.label_2.setNum)
        self.dial_2.valueChanged['int'].connect(self.label_2.setNum)
        self.pushButton.clicked.connect(self.set_Label_Text)
        self.toolButton.clicked.connect(self.set_Label_Text)
        self.radioButton.clicked.connect(self.set_Label_Text)
        self.checkBox.clicked.connect(self.set_Label_Text)
        self.buttonBox.accepted.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mw = MainWindow

    def set_Label_Text(self):
        text = self.mw.sender().text()
        self.label.setText(text)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyShine"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.toolButton.setText(_translate("MainWindow", "Click me..."))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))
        self.label.setText(_translate("MainWindow", "Buttons"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Buttons"))
        self.label_2.setText(_translate("MainWindow", "Dial Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Dials"))
        self.label_3.setText(_translate("MainWindow", "Slider Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Sliders"))
        self.menuPyshine.setTitle(_translate("MainWindow", "File"))
        self.menuSubmenu.setTitle(_translate("MainWindow", "Submenu"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.statusbar.setStatusTip(_translate("MainWindow", "Pyshine"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Click to Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionitem1.setText(_translate("MainWindow", "item1"))
        self.actionitem_2.setText(_translate("MainWindow", "item2"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMaximize.setShortcut(_translate("MainWindow", "Shift+M"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionNormal.setShortcut(_translate("MainWindow", "Shift+N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())