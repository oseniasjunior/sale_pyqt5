import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from views.controllers import MainWindowController

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons

app = QApplication(sys.argv)

window = MainWindowController()
window.showMaximized()
sys.exit(app.exec_())
