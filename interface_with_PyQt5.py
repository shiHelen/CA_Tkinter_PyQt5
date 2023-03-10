# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_template_LAAAST.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.Qt import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 69, 741, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 460, 731, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(205, 215, 255);\n"
"border-radius: 10px; \n"
"border: 2px solid #094065;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(205, 215, 255);\n"
"border-radius: 10px; \n"
"border: 2px solid #094065;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setStyleSheet("background-color: rgb(239, 222, 205);")
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 6, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(205, 215, 255);\n"
"border-radius: 10px; \n"
"border: 2px solid #094065;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 2, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setStyleSheet("background-color: rgb(239, 222, 205);")
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 6, 2, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(233, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 4, 3, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 3, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 3, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(205, 215, 255);\n"
"border-radius: 10px; \n"
"border: 2px solid #094065;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 440, 171, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(205, 215, 255);\n"
"border-radius: 10px; \n"
"border: 2px solid #094065;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(-10, 0, 801, 891))
        self.label_13.setStyleSheet("background-image: url(:/newPrefix/v1.jpg);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 0, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 450, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 240, 253);\n"
"")
        self.lineEdit.setFont(font)
        self.lineEdit.setText("x ** 3 - 5.9 * x ** 2 + 11.1 * x - 6.7")
        self.lineEdit.setObjectName("lineEdit")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 40, 50, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("1")
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 0, 400, 42))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(610, 40, 50, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 240, 253);")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("3")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13.raise_()
        self.gridLayoutWidget.raise_()
        self.pushButton_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_14.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????? ?????????????? ???????????????????? ?????????????????? ??????????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "????????????????"))
        self.pushButton.setText(_translate("MainWindow", "????????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "??????????????????"))
        self.label_4.setText(_translate("MainWindow", "epsilon"))
        self.label_6.setText(_translate("MainWindow", "a"))
        self.label_9.setText(_translate("MainWindow", "?????????????????? ?????????????????????? x1:"))
        self.label_5.setText(_translate("MainWindow", "b"))
        self.label_7.setText(_translate("MainWindow", "?????????? ?????????????????????? ??????????????:"))
        self.label_11.setText(_translate("MainWindow", "?????????? ??????????????:"))
        self.label_10.setText(_translate("MainWindow", "epsilon"))
        self.pushButton_5.setText(_translate("MainWindow", "??????????????????"))
        self.label_15.setText(_translate("MainWindow", "?????????????????? ?????????????????????? x0:"))
        self.label_12.setText(_translate("MainWindow", "???????????? ??????????????:"))
        self.pushButton_2.setText(_translate("MainWindow", "?????????????????? ????????????"))
        self.label_14.setText(_translate("MainWindow", "?????????????????????? ??????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????????? ?????????????????? [a,b]:"))
        self.pushButton_5.clicked.connect(self.half_div)
        self.pushButton.clicked.connect(self.clearHaldDivM)
        self.pushButton_4.clicked.connect(self.secant)
        self.pushButton_6.clicked.connect(self.clearSecant)

    def clearSecant(self):      # ?????????????? ???????? ???????????????????? ???????????? ??????????????
            self.textEdit_4.setText(" ")

    def clearHaldDivM(self):    # ?????????????? ???????? ???????????????????? ???????????? ?????????????????????? ??????????????
            self.textEdit_3.setText(" ")

    def half_div(self):         # ?????????? ?????????????????????? ??????????????
            a = float(self.lineEdit_6.text())   # ???????????????????? ?????????????????? ????????????????
            b = float(self.lineEdit_5.text())
            eps = float(self.lineEdit_4.text())
            c = (a + b) / 2
            n = 0
            while (b - a) >= 2 * eps:
                    n += 1
                    if f(c) == 0:
                            return c
                    if f(a) * f(c) < 0:
                            b = c
                    else:
                            a = c
                    c = (a + b) / 2
            self.textEdit_3.setText("????????????: " + str(c) + '\n' + "??????????????: " + str("{:e}".format(-f(c))) + '\n' + "?????????? ????????????????: " + str(n))   # ???????????????? ???????????????????? ?? ???????? ????????????

    def secant(self):     # ?????????? ??????????????
            m = 0
            x0 = float(self.lineEdit_7.text())      # ???????????????????? ?????????????????? ????????????????
            x1 = float(self.lineEdit_8.text())
            epsilon = float(self.lineEdit_9.text())
            while math.fabs(x1 - x0) > epsilon:
                    xk = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
                    x0 = x1
                    x1 = xk
                    m += 1
            self.textEdit_4.setText("????????????: " + str(x1) + '\n' + "??????????????: " + str("{:e}".format(-f(x1))) + '\n' + "?????????? ????????????????: " + str(m))    # ???????????????? ???????????????????? ?? ???????? ????????????


class MplCanvas(FigureCanvas):      # ?????????? ?????? ???????????????????? ?????????????? ?? ???????? ????????????????????
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        super(MplCanvas, self).__init__(self.fig, *args, **kwargs)

    def plot(self, x, y):       # ?????????????? ?????? ?????????????????? ??????????????
        self.fig.clear()        # ?????????????? ???????? ?????? ????????????????????
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x, y, color="darkmagenta", label="y(x)", linewidth=2)      # ???????????????????? ??????????????
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.legend()
        self.ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.draw()


class TEST(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TEST, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.plot_graph)      # ?????????????????? ?????????????? ???? ???????????? ???????????????????? ??????????????
        self.canavas = MplCanvas()
        self.canavas.setMinimumSize(300, 300)
        self.toolbar = NavigationToolbar(self.canavas, self)
        self.verticalLayout.addWidget(self.canavas)
        self.verticalLayout.addWidget(self.toolbar)
        self.toolbar.hide()
        self.setStyleSheet('.QWidget {background-image: url(v1.jpg);}')

    def plot_graph(self):           # ?????????????? ?????? ?????????????????? ??????????????
        a = float(self.lineEdit_2.text())           # ???????????????????? ?????????????????? ????????????????
        b = float(self.lineEdit_3.text())
        mystr = self.lineEdit.text()        # ???????????????? ???????????????????????? ?????????????????? ?? ???????? ????????????
        exec('f = lambda x:' + mystr, globals())        # ???????????????????????????? ?????????????????? ???? ???????? ???????????? ?? ?????????????? f(x)
        X = np.linspace(a, b, 300)
        Y = [f(x) for x in X]
        self.canavas.plot(X, Y)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TEST()
    ui.show()
    sys.exit(app.exec_())
