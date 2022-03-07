from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QTableWidgetItem, QTableWidget, QCheckBox, QHeaderView, \
    QHBoxLayout

from core.connection import Database
from core import helpers
from views.department import Ui_Department
from views.mainwindow import Ui_MainWindow
from views.marital_status import Ui_MaritalStatus
from views.marital_status_item import Ui_MaritalStatusItem


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowController, self).__init__(parent=parent)
        self.setupUi(self)
        self.actionEstado_Civil.triggered.connect(self._on_click_marital_status)
        self.actionDepartamento.triggered.connect(self._on_click_department)

    def _on_click_marital_status(self):
        helpers.clear_layout(self.body.layout())
        form = MaritalStatusController(parent=self)
        self.body.layout().addWidget(form)

    def _on_click_department(self):
        helpers.clear_layout(self.body.layout())
        form = DepartmentController(parent=self)
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


class DepartmentController(QWidget, Ui_Department):
    def __init__(self, parent=None):
        super(DepartmentController, self).__init__(parent=parent)
        self.setupUi(self)
        self.table_department.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.btn_search.clicked.connect(self._search)
        self.db = Database()
        self._search()

    def _search(self):
        results = self.db.search('department')
        self.table_department.setRowCount(len(results))

        for index, item in enumerate(results):
            code = QTableWidgetItem()
            code.setText(str(item['id']))

            name = QTableWidgetItem()
            name.setText(str(item['name']))

            modified_at = QTableWidgetItem()
            modified_at.setText(helpers.format_date(item['modified_at']))

            active = QCheckBox()
            active.setChecked(item['active'])

            layout = QHBoxLayout()
            layout.addWidget(active)

            wd = QWidget()
            wd.setLayout(layout)

            self.table_department.setItem(index, 0, code)
            self.table_department.setItem(index, 1, name)
            self.table_department.setItem(index, 2, modified_at)
            self.table_department.setCellWidget(index, 3, wd)
