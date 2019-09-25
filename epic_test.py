import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        self.epic_level = 0

        super(Form, self).__init__(parent)
        self.setWindowTitle("Epic")
        self.label = QLabel("Epic level:")
        self.output = QLineEdit(f"{self.epic_level}")
        self.output.setFocusPolicy(Qt.NoFocus)

        self.epic = QPushButton("Epic")
        self.notepic = QPushButton("Not epic")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.output)
        layout.addWidget(self.epic)
        layout.addWidget(self.notepic)

        self.setLayout(layout)
        self.epic.clicked.connect(self.more_epic)
        self.notepic.clicked.connect(self.less_epic)

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
