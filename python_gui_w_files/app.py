import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QComboBox, QPushButton,
                             QTableWidget, QTableWidgetItem, QMessageBox,
                             QHeaderView, QLineEdit)

DATA_FILE = "students.txt"

class StudentManagementSystem(QWidget):
    def __init__(self):
        # class constructor
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.resize(800, 400)
        self.selected_row = None
        self.create_ui()
        self.load_students()

    def create_ui(self):
        main_layout = QHBoxLayout(self)
        sidebar = QVBoxLayout()

        # Name
        name_label = QLabel("Student Name:")
        # StudentManagementSystem.name_input
        self.name_input = QLineEdit()
        sidebar.addWidget(name_label)
        sidebar.addWidget(self.name_input)

        # Year
        year_label = QLabel("Year:")
        self.year_input = QComboBox()
        years = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        self.year_input.addItems(years)
        sidebar.addWidget(year_label)
        sidebar.addWidget(self.year_input)

        # Program
        program_label = QLabel("Program:")
        self.program_input = QLineEdit()
        sidebar.addWidget(program_label)
        sidebar.addWidget(self.program_input)

        # Buttons
        self.add_btn = QPushButton("Add")
        self.update_btn = QPushButton("Update")
        self.delete_btn = QPushButton("Delete")

        # Events
        self.add_btn.clicked.connect(self.add_student)
        self.update_btn.clicked.connect(self.update_student)
        self.delete_btn.clicked.connect(self.delete_student)

        sidebar.addWidget(self.add_btn)
        sidebar.addWidget(self.update_btn)
        sidebar.addWidget(self.delete_btn)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        headers = ["Name", "Year", "Program"]
        self.table.setHorizontalHeaderLabels(headers)
        # Remove table numbers
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellClicked.connect(self.fill_inputs_from_table)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        main_layout.addLayout(sidebar, 1)
        main_layout.addWidget(self.table, 3)

    # Functions
    def save_students(self):
        # w = write
        with open(DATA_FILE, "w") as file:
            # range(3)
            for row in range(self.table.rowCount()):
                name = self.table.item(row, 0).text()
                year = self.table.item(row, 1).text()
                program = self.table.item(row, 2).text()
                file.write(f"{name}|{year}|{program}\n")

    def load_students(self):
        # r = read
        with open(DATA_FILE, "r") as file:
            for line in file:
                name, year, program = line.split("|")
                self.add_row_to_table(name, year, program)

    def add_student(self):
        name = self.name_input.text().strip()
        year = self.year_input.currentText()
        program = self.program_input.text().strip()

        if not name or not program:
            QMessageBox.warning(self, "Input Error", "Please fill all the fields!")
            return

        self.add_row_to_table(name, year, program)
        self.save_students()
        self.clear_inputs()

    def add_row_to_table(self, name, year, program):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(name))
        self.table.setItem(row_position, 1, QTableWidgetItem(year))
        self.table.setItem(row_position, 2, QTableWidgetItem(program))

    def clear_inputs(self):
        self.name_input.clear()
        self.program_input.clear()
        self.year_input.setCurrentIndex(0)

    def fill_inputs_from_table(self, row):
        self.selected_row = row
        self.name_input.setText(self.table.item(row, 0).text())
        self.year_input.setCurrentText(self.table.item(row, 1).text())
        self.program_input.setText(self.table.item(row, 2).text())

    def update_student(self):
        if self.selected_row is None:
            QMessageBox.warning(self, "Selection Error", "Please select a student to update.")
            return

        new_name = self.name_input.text().strip()
        new_year = self.year_input.currentText()
        new_program = self.program_input.text().strip()

        if not new_name or not new_program:
            QMessageBox.warning(self, "Input Error", "Please fill all the fields!")
            return

        self.table.setItem(self.selected_row, 0, QTableWidgetItem(new_name))
        self.table.setItem(self.selected_row, 1, QTableWidgetItem(new_year))
        self.table.setItem(self.selected_row, 2, QTableWidgetItem(new_program))
        self.save_students()
        self.clear_inputs()

    def delete_student(self):
        if self.selected_row is None:
            QMessageBox.warning(self, "Selection Error", "Please select a student to delete.")
            return

        self.table.removeRow(self.selected_row)
        self.save_students()
        self.clear_inputs()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = StudentManagementSystem()
    window.show()
    sys.exit(app.exec())
