import sys
import os
import pathlib
import pprint
import json
import pandas
from PyQt5 import QtWidgets, uic, QtCore
from main_window import Ui_MainWindow

steam_cmd = 'steam://run/594570'
work_dir = os.environ['APPDATA'] + '\\MyModManager'
failsafe = work_dir + '\\failsafe.dat'

if not os.path.exists(failsafe):
    with open(failsafe, 'w', encoding="utf8") as outfile:
        json.dump(mod_list, outfile)

if not os.path.exists(work_dir):
    os.makedirs(work_dir)

class ModConfig:
    """ load mod Json data and structure """
    def __init__(self):
        self.raw_list = []
        self.mod_data = []

    def readLauncherConfig(self):
        launcher_dir = os.environ['APPDATA'] + '\\The Creative Assembly\\Launcher'
        glob_path = pathlib.Path(launcher_dir)
        moddata = [ str(fname) for fname in glob_path.glob("*-moddata.dat") ]
        self.readJsonData(moddata[0])

    def readJsonData(self, json_file):
        with open(json_file, encoding='utf8') as json_data:
            self.raw_list = json.load(json_data)

class MyModManager(QtWidgets.QMainWindow):
    """ Main application class """
    def __init__(self):
        super(MyModManager, self).__init__()
        self.title = 'Simple Total War: Warhammer II Mod Manager'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.launchGameBtn.clicked.connect(self.launchGameClicked)
        self.ui.refreshBtn.clicked.connect(self.refreshBtnClicked)
        self.populateTable()
        self.setWindowTitle(self.title)

    def populateTable(self):
        mods_table_cols = ['order', 'active', 'uuid', 'game', 'packfile', 'name', 'category', 'short', 'owned']
        hide_cols = ['game', 'packfile', 'owned']
        mods_table = self.ui.modListTbl
        mods_table.setColumnCount(len(mods_table_cols))
        mods_table.verticalHeader().setVisible(False)
        mods_table.setHorizontalHeaderLabels(mods_table_cols)

        for index, col in enumerate(mods_table_cols):
            if col in hide_cols:
                mods_table.setColumnHidden(index, True) 

        for row, mod_row in enumerate(mod_list):
            mods_table.insertRow(mods_table.rowCount())
            for col, value in enumerate(mod_row):
                row_item = QtWidgets.QTableWidgetItem()
                if value == 'active':
                    row_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    row_item.setCheckState(mod_row[value])
                else:
                    row_item.setData(QtCore.Qt.DisplayRole, mod_row[value])
                mods_table.setItem(row, mods_table_cols.index(value), row_item)

        mods_table.resizeColumnsToContents()

    def refreshBtnClicked(self):
        self.populateTable()

    def launchGameClicked(self):
        os.startfile(steam_cmd)

if __name__ == '__main__':
    mod_manager_app = QtWidgets.QApplication(sys.argv)
    mod_manager = MyModManager()
    mod_manager.show()
    sys.exit(mod_manager_app.exec_())