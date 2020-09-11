# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from gui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 598)
        icon = QIcon()
        icon.addFile(u":/icons/images/app.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/images/app.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QSize(200, 200))
        self.tableView.setMaximumSize(QSize(1000, 1000))
        self.tableView.setBaseSize(QSize(300, 300))
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setIconSize(QSize(50, 50))
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_9.addWidget(self.tableView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(10, 20))
        self.frame_3.setBaseSize(QSize(10, 10))
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.name_player = QLineEdit(self.frame_3)
        self.name_player.setObjectName(u"name_player")

        self.gridLayout_8.addWidget(self.name_player, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_8.addWidget(self.pushButton, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tableView_2 = QTableView(self.tab_2)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setAlternatingRowColors(True)
        self.tableView_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_2.setIconSize(QSize(50, 50))
        self.tableView_2.setSortingEnabled(True)
        self.tableView_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_7.addWidget(self.tableView_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_6 = QGridLayout(self.tab_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableView_3 = QTableView(self.tab_7)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setAlternatingRowColors(True)
        self.tableView_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_3.setIconSize(QSize(50, 50))
        self.tableView_3.setSortingEnabled(True)
        self.tableView_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_3.horizontalHeader().setStretchLastSection(True)
        self.tableView_3.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_6.addWidget(self.tableView_3, 2, 0, 1, 1)

        self.frame = QFrame(self.tab_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 3)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_10.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.quality = QComboBox(self.frame)
        self.quality.setObjectName(u"quality")

        self.gridLayout_10.addWidget(self.quality, 1, 0, 1, 2)


        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.name_player_3 = QLineEdit(self.frame_5)
        self.name_player_3.setObjectName(u"name_player_3")

        self.gridLayout_11.addWidget(self.name_player_3, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_11.addWidget(self.label_8, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_11.addWidget(self.pushButton_4, 2, 2, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)

        self.tableView_4 = QTableView(self.tab_3)
        self.tableView_4.setObjectName(u"tableView_4")
        self.tableView_4.setAlternatingRowColors(True)
        self.tableView_4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_4.setIconSize(QSize(50, 50))
        self.tableView_4.setSortingEnabled(True)
        self.tableView_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_4.horizontalHeader().setStretchLastSection(True)
        self.tableView_4.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_4.addWidget(self.tableView_4, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_2 = QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(10, 20))
        self.frame_4.setBaseSize(QSize(10, 10))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 660, 121))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.name_player_2 = QLineEdit(self.widget)
        self.name_player_2.setObjectName(u"name_player_2")

        self.verticalLayout.addWidget(self.name_player_2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_3.addWidget(self.tabWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.compare_price_by_player)
        self.pushButton.clicked.connect(MainWindow.search_by_name)
        self.pushButton_3.clicked.connect(MainWindow.best_5_players)
        self.pushButton_4.clicked.connect(MainWindow.calculate_valutation_attack)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FIFA FUT WIKI", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FIFA20 FUT WIKI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Inserimento / rimozione / visualizzazione", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Inserisci il nome del giocatore da ricercare", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cerca", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Ricerca per nome", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"In questa sezione verranno visualizzati i migliori 5 giocatori (selezionati in base alla qualit\u00e0 della carta, scelta dall'utente), ordinati per overall", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cerca", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Migliori 5 giocatori", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Inserisci il nome del giocatore", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Cerca", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"In questa sezione varr\u00e0 visualizzato l'attributo calcolato \"valutazione attacco\" per il giocatore scelto dall'utente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Valutazione attacco", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"In questa sezione verr\u00e0 visualizzato il grafico comparativo per i prezzi delle varie piattaforme di gioco, dato un giocatore scelto dall'utente", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Inserisci il nome del giocatore scelto", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cerca", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Andamento prezzi per giocatore", None))
    # retranslateUi

