import math
import sys
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QDoubleSpinBox,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QGroupBox,
)

def reelle_loesninger_til_andengradsligning(a, b, c):
    d = (b**2) - (4 * a * c)
    if a == 0:
        if b == 0:
            if c == 0:
                return "Uendeligt mange løsninger"
            else:
                return "Ingen løsninger"
        else:
            x = -c / b
            return f"Én løsning: x = {x}"

    if d < 0:
        return "Ingen løsninger"
    elif d == 0:
        x = -b / (2 * a)
        return f"Én løsning: x = {x}"
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"To rødder: x1 = {x1}, x2 = {x2}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Andengradsligningsløser")
        self.setMinimumWidth(700)

        title = QLabel("Andengradsligningsløser")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.equation_label = QLabel("Løsning af andengradsligning på formen: a·x² + b·x + c = 0")
        self.equation_label.setAlignment(Qt.AlignCenter)

        input_group = QGroupBox("Indtast værdier for a, b og c:")
        input_layout = QGridLayout()
        input_layout.addWidget(QLabel("a:"), 0, 0)
        self.a_input = QDoubleSpinBox()
        self.a_input.setRange(-100, 100)
        self.a_input.setValue(1.0)
        input_layout.addWidget(self.a_input, 0, 1)

        input_layout.addWidget(QLabel("b:"), 1, 0)
        self.b_input = QDoubleSpinBox()
        self.b_input.setRange(-100, 100)
        self.b_input.setValue(0.0)
        input_layout.addWidget(self.b_input, 1, 1)

        input_layout.addWidget(QLabel("c:"), 2, 0)
        self.c_input = QDoubleSpinBox()
        self.c_input.setRange(-100, 100)
        self.c_input.setValue(0.0)
        input_layout.addWidget(self.c_input, 2, 1)
        input_group.setLayout(input_layout)

        self.calculate_button = QPushButton("Bestem")
        self.calculate_button.setStyleSheet("padding: 8px 24px; font-size: 14px;")
        self.calculate_button.clicked.connect(self.beregn)

        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)
        self.result_field.setFont(QFont("Arial", 14))
        self.result_field.setAlignment(Qt.AlignCenter)
        self.result_field.setStyleSheet("border: 1px solid #ccc; padding: 8px;")

        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.equation_label)
        main_layout.addSpacing(10)
        main_layout.addWidget(input_group)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.calculate_button, alignment=Qt.AlignCenter)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.result_field)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setWindowIcon(QIcon("catsittingverycomfortable.png"))

    def beregn(self):
        a = self.a_input.value()
        b = self.b_input.value()
        c = self.c_input.value()
        result = reelle_loesninger_til_andengradsligning(a, b, c)
        self.result_field.setText(result)

        self.equation_label.setText(f"Ligning: {a}·x² + {b}·x + {c} = 0")

andengradsligningsloeser = QApplication(sys.argv)
vindue = MainWindow()
vindue.show()
andengradsligningsloeser.exec()