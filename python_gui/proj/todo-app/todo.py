from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do App")
        self.resize(400, 400)

        # Main layout
        layout = QVBoxLayout()

        # Input and button
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.add_btn = QPushButton("Add Task")
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_btn)

        # Task list
        self.task_list = QListWidget()

        # Remove button
        self.remove_btn = QPushButton("Remove Selected Task")

        # Add widgets to layout
        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)
        layout.addWidget(self.remove_btn)
        self.setLayout(layout)

        # Signals
        self.add_btn.clicked.connect(self.add_task)
        self.remove_btn.clicked.connect(self.remove_task)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def remove_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to remove!")

if __name__ == "__main__":
    app = QApplication([])

    # Load external QSS
    with open("style.qss", "r") as f:
        qss = f.read()
        app.setStyleSheet(qss)

    window = ToDoApp()
    window.show()
    app.exec_()
