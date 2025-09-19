import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI")
        self.resize(300, 200)
        self.title = QLabel("My Project")
        self.label = QLabel("Name")
        self.name_input = QLineEdit()
        self.submit_btn = QPushButton("Submit")
        self.output = QLabel("Output")

        # Layouts
        master_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()

        master_layout.addWidget(self.title, alignment=Qt.AlignHCenter)

        horizontal_layout.addWidget(self.label)
        horizontal_layout.addWidget(self.name_input)

        master_layout.addLayout(horizontal_layout)

        master_layout.addWidget(self.submit_btn)

        master_layout.addWidget(self.output, alignment=Qt.AlignHCenter)

        # Events
        self.submit_btn.clicked.connect(self.display_name)

        self.setLayout(master_layout)

    def display_name(self):
        user_name = self.name_input.text()
        self.output.setText(user_name)
        self.name_input.setText("")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())