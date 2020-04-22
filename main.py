import sys
import os
import pathlib
import pprint
import json
from PyQt5 import QtWidgets, uic
from main_window import Ui_MainWindow

steam_cmd = 'steam://run/594570'
work_dir = os.environ['APPDATA'] + '\\MyModManager'
failsafe = work_dir + '\\failsafe.dat'
launcher_dir = os.environ['APPDATA'] + '\\The Creative Assembly\\Launcher'
glob_path = pathlib.Path(launcher_dir)
moddata = [ str(fname) for fname in glob_path.glob("*-moddata.dat") ]
print(moddata)

with open(moddata[0], encoding="utf8") as raw_data:
    mod_list = json.load(raw_data)

if not os.path.exists(failsafe):
    with open(failsafe, 'w', encoding="utf8") as outfile:
        json.dump(mod_list, outfile)

for mod in mod_list:
    print(str(mod['name']) + ' - Active: ' + str(mod['active']))


if not os.path.exists(work_dir):
    os.makedirs(work_dir)

class MyModManager(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyModManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.launchGameBtn.clicked.connect(self.launchGameClicked)

    def launchGameClicked(self):
        os.startfile(steam_cmd)

mod_manager_app = QtWidgets.QApplication([])

mod_manager = MyModManager()

mod_manager.show()

sys.exit(mod_manager_app.exec())