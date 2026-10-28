from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        self.display = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+'
        ]

        row = col = 0
        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        text = self.sender().text()
        if text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())
