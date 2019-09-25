import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.epic_level = 0

        self.setWindowTitle("Grid")
        grid = QGridLayout()
        self.setLayout(grid)

        self.label = QLabel("Epic level:")
        self.output = QLineEdit(f"{self.epic_level}")
        self.output.setFocusPolicy(Qt.NoFocus)

        self.epic = QPushButton("Epic")
        self.notepic = QPushButton("Not epic")
        self.epic.clicked.connect(self.more_epic)
        self.notepic.clicked.connect(self.less_epic)

        grid.addWidget(self.label, 0, 0, 1, 2)
        grid.addWidget(self.output, 1, 0, 1, 2)
        grid.addWidget(self.epic, 2, 1, 1, 1)
        grid.addWidget(self.notepic, 2, 0, 1, 1)

    def update_output(self):
        self.output.text()
        self.output.setText(f"{self.epic_level}")

    def more_epic(self):
        self.epic_level += 1
        self.update_output()

    def less_epic(self):
        self.epic_level -= 1
        self.update_output()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
