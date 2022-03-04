from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog

from views import helpers
from views.mainwindow import Ui_MainWindow
from views.marital_status import Ui_MaritalStatus
from views.marital_status_item import Ui_MaritalStatusItem


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowController, self).__init__(parent=parent)
        self.setupUi(self)
        self.actionEstado_Civil.triggered.connect(self._on_click_marital_status)

    def _on_click_marital_status(self):
        helpers.clear_layout(self.body.layout())
        form = MaritalStatusController(parent=self)
        self.body.layout().addWidget(form)


class MaritalStatusController(QWidget, Ui_MaritalStatus):
    def __init__(self, parent=None):
        super(MaritalStatusController, self).__init__(parent=parent)
        self.setupUi(self)
        self.btn_add.clicked.connect(self._on_click_add)

    def _on_click_add(self):
        form = MaritalStatusItemController(parent=self)
        form.exec_()


class MaritalStatusItemController(QDialog, Ui_MaritalStatusItem):
    def __init__(self, parent=None):
        super(MaritalStatusItemController, self).__init__(parent=parent)
        self.setupUi(self)
