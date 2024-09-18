# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 801, 441))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 440, 811, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titulo_input = QLineEdit(self.horizontalLayoutWidget)
        self.titulo_input.setObjectName(u"titulo_input")

        self.horizontalLayout.addWidget(self.titulo_input)

        self.descripcion_input = QLineEdit(self.horizontalLayoutWidget)
        self.descripcion_input.setObjectName(u"descripcion_input")

        self.horizontalLayout.addWidget(self.descripcion_input)

        self.hora_limite_input = QLineEdit(self.horizontalLayoutWidget)
        self.hora_limite_input.setObjectName(u"hora_limite_input")

        self.horizontalLayout.addWidget(self.hora_limite_input)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 490, 801, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.agregar_button = QPushButton(self.horizontalLayoutWidget_2)
        self.agregar_button.setObjectName(u"agregar_button")

        self.horizontalLayout_2.addWidget(self.agregar_button)

        self.eliminar_button = QPushButton(self.horizontalLayoutWidget_2)
        self.eliminar_button.setObjectName(u"eliminar_button")

        self.horizontalLayout_2.addWidget(self.eliminar_button)

        self.completar_button = QPushButton(self.horizontalLayoutWidget_2)
        self.completar_button.setObjectName(u"completar_button")

        self.horizontalLayout_2.addWidget(self.completar_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lista de Tareas", None))
        self.titulo_input.setText("")
        self.titulo_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.descripcion_input.setText("")
        self.descripcion_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.hora_limite_input.setText("")
        self.hora_limite_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hora l\u00edmite (HH:MM)", None))
        self.agregar_button.setText(QCoreApplication.translate("MainWindow", u"Agregar Tarea", None))
        self.eliminar_button.setText(QCoreApplication.translate("MainWindow", u"Eliminar Tarea", None))
        self.completar_button.setText(QCoreApplication.translate("MainWindow", u"Marcar como Completada", None))
    # retranslateUi

