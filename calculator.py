import sys
from PySide2.QtCore import Qt, Slot, QObject, Signal
from PySide2.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text = ""

        self.setWindowTitle("Calculator")
        grid = QGridLayout()
        self.setLayout(grid)

        self.output = QLineEdit(f"0")
        self.output.setFocusPolicy(Qt.NoFocus)

        self.numbers = [QPushButton(f"{n}") for n in range(0, 10)]
        self.add = QPushButton("+")
        self.sub = QPushButton("-")
        self.mul = QPushButton("*")
        self.div = QPushButton("/")
        self.clr = QPushButton("CLR")

        grid.addWidget(self.output, 0, 0, 1, 4)
        grid.addWidget(self.numbers[1], 1, 0, 1, 1)
        grid.addWidget(self.numbers[2], 1, 1, 1, 1)
        grid.addWidget(self.numbers[3], 1, 2, 1, 1)
        grid.addWidget(self.numbers[4], 2, 0, 1, 1)
        grid.addWidget(self.numbers[5], 2, 1, 1, 1)
        grid.addWidget(self.numbers[6], 2, 2, 1, 1)
        grid.addWidget(self.numbers[7], 3, 0, 1, 1)
        grid.addWidget(self.numbers[8], 3, 1, 1, 1)
        grid.addWidget(self.numbers[9], 3, 2, 1, 1)
        grid.addWidget(self.numbers[0], 4, 0, 1, 2)

        grid.addWidget(self.add, 1, 3, 1, 1)
        grid.addWidget(self.sub, 2, 3, 1, 1)
        grid.addWidget(self.mul, 3, 3, 1, 1)
        grid.addWidget(self.div, 4, 3, 1, 1)
        grid.addWidget(self.clr, 4, 2, 1, 1)

        self.numbers[0].clicked.connect(lambda: self.number_clicked(0))
        self.numbers[1].clicked.connect(lambda: self.number_clicked(1))
        self.numbers[2].clicked.connect(lambda: self.number_clicked(2))
        self.numbers[3].clicked.connect(lambda: self.number_clicked(3))
        self.numbers[4].clicked.connect(lambda: self.number_clicked(4))
        self.numbers[5].clicked.connect(lambda: self.number_clicked(5))
        self.numbers[6].clicked.connect(lambda: self.number_clicked(6))
        self.numbers[7].clicked.connect(lambda: self.number_clicked(7))
        self.numbers[8].clicked.connect(lambda: self.number_clicked(8))
        self.numbers[9].clicked.connect(lambda: self.number_clicked(9))

        self.clr.clicked.connect(lambda: self.clear())

    def clear(self):
        self.text = "0"
        self.update_output()

    def number_clicked(self, num):
        if self.text == "0":
            self.text = str(num)
        else:
            self.text += str(num)
        self.update_output()

    def update_output(self):
        self.output.setText(f"{self.text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
