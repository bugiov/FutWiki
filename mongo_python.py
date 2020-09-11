from PySide2 import QtWidgets, QtUiTools
from PySide2.QtCharts import QtCharts
from PySide2 import QtGui
from PySide2 import QtCore
from gui import main
from lib import databaseOperations
from lib import customModel

import sys
from bson.json_util import dumps
import json
import matplotlib.pyplot as plt
import numpy as np

class PythonMongoDB(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(PythonMongoDB, self).__init__()
        self.setupUi(self)

        self.user_data = databaseOperations.get_multiple_data()
        self.model = customModel.CustomTableModel(self.user_data)
        self.delegate = customModel.InLineEditDelegate()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(self.delegate)
        #self.tableView.setItemDelegateForColumn(1, customModel.ProfilePictureDelegate())
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.context_menu)
        self.tableView.verticalHeader().setDefaultSectionSize(50)
        self.tableView.setColumnWidth(0, 30)
        self.tableView.hideColumn(0)

        all_quality = databaseOperations.get_all_quality()
        for q in all_quality:
            self.quality.addItem(q)



    def context_menu(self):
        menu = QtWidgets.QMenu()
        add_data = menu.addAction("Inserisci nuovo")
        add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: self.model.insertRows())
        if self.tableView.selectedIndexes():
            remove_data = menu.addAction("Rimuovi")
            remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: self.model.removeRows(self.tableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def search_by_name(self):
        name = self.name_player.text()
        data_2 = databaseOperations.get_data_by_player_name(name)
        model_2 = customModel.CustomTableModel(data_2)
        self.tableView_2.setModel(model_2)
        self.tableView_2.hideColumn(0)

    def best_5_players(self):
        quality_selected = self.quality.currentText()
        data_3 = databaseOperations.get_best_5_players(quality_selected)
        model_3 = customModel.CustomTableModel(data_3)
        self.tableView_3.setModel(model_3)
        self.tableView_3.hideColumn(0)

    def calculate_valutation_attack(self):
        player_name = self.name_player_3.text()
        if player_name:
            data_4 = databaseOperations.get_valutation_attack(player_name)
            model_4 = customModel.CustomTableModel(data_4)
            self.tableView_4.setModel(model_4)
            self.tableView_4.hideColumn(0)

    def compare_price_by_player(self):
        player_name = self.name_player_2.text()
        data_5 = json.loads(dumps(databaseOperations.get_one_player_by_name(player_name)))
        my_app.addmpl(data_5)

    def addmpl(self, data):
        n_groups = 3
        set_min = ([data['pc_min'], data['ps4_min'], data['xbox_min']])
        set_max = ([data['pc_max'], data['ps4_max'], data['xbox_max']])
        set_last = ([data['pc_last'], data['ps4_last'], data['xbox_last']])

        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.25
        opacity = 0.8

        rects1 = plt.bar(index - bar_width, set_min, bar_width,
                         alpha=opacity,
                         color='b',
                         label='Minimo')
        rects2 = plt.bar(index, set_max, bar_width,
                         alpha=opacity,
                         color='g',
                         label='Massimo')
        rects3 = plt.bar(index + bar_width, set_last, bar_width,
                         alpha=opacity,
                         color='r',
                         label='Ultimo')

        plt.xlabel('Piattaforme')
        plt.ylabel('Prezzo')
        plt.title('Comparazione prezzi delle piattaforme')
        plt.xticks(index, ('PC', 'PS4', 'XBOX'))
        plt.legend()

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    my_app = PythonMongoDB()
    my_app.show()
    app.exec_()
