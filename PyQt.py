from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.setWindowTitle('QQMes_Change')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.srcTextEdit = QtWidgets.QTextEdit(self.centralwidget)  # 左侧源文字
        self.srcTextEdit.setObjectName("srcTextEdit")
        self.verticalLayout.addWidget(self.srcTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.changeButton = QtWidgets.QPushButton(self.centralwidget)   # 转换按钮
        self.changeButton.setMinimumSize(QtCore.QSize(75, 50))
        self.changeButton.setMaximumSize(QtCore.QSize(75, 50))
        self.changeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dataset/button_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeButton.setIcon(icon)
        self.changeButton.setIconSize(QtCore.QSize(75, 50))
        self.changeButton.setObjectName("changeButton")
        self.verticalLayout_3.addWidget(self.changeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.destTextEdit = QtWidgets.QTextEdit(self.centralwidget)     # 右侧修改后文字
        self.destTextEdit.setObjectName("destTextEdit")
        self.verticalLayout_2.addWidget(self.destTextEdit)

        self.copyButton = QtWidgets.QPushButton("copy", self.centralwidget)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout_2.addWidget(self.copyButton)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.resize(1080, 600)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
