from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLineEdit, QLabel, QMessageBox
)
from PySide6.QtCore import Qt
from main import Tarea, Lista_de_tareas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lista_de_tareas = Lista_de_tareas()

        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(300, 300, 400, 300)

        # Layout principal
        main_layout = QVBoxLayout()

        # Widget de lista para mostrar las tareas
        self.list_widget = QListWidget()
        main_layout.addWidget(self.list_widget)

        # Campos de entrada
        input_layout = QHBoxLayout()
        self.titulo_input = QLineEdit()
        self.titulo_input.setPlaceholderText("Título")
        self.descripcion_input = QLineEdit()
        self.descripcion_input.setPlaceholderText("Descripción")
        self.hora_limite_input = QLineEdit()
        self.hora_limite_input.setPlaceholderText("Hora límite (HH:MM)")
        input_layout.addWidget(self.titulo_input)
        input_layout.addWidget(self.descripcion_input)
        input_layout.addWidget(self.hora_limite_input)
        main_layout.addLayout(input_layout)

        # Botones
        button_layout = QHBoxLayout()
        agregar_button = QPushButton("Agregar Tarea")
        agregar_button.clicked.connect(self.agregar_tarea)
        eliminar_button = QPushButton("Eliminar Tarea")
        eliminar_button.clicked.connect(self.eliminar_tarea)
        completar_button = QPushButton("Marcar como Completada")
        completar_button.clicked.connect(self.marcar_como_completada)
        button_layout.addWidget(agregar_button)
        button_layout.addWidget(eliminar_button)
        button_layout.addWidget(completar_button)
        main_layout.addLayout(button_layout)

        # Widget principal
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def agregar_tarea(self):
        titulo = self.titulo_input.text()
        descripcion = self.descripcion_input.text()
        hora_limite = self.hora_limite_input.text()

        if titulo and descripcion and hora_limite:
            tarea = Tarea(titulo, descripcion, hora_limite)
            self.lista_de_tareas.agregar_tarea(tarea)
            self.list_widget.addItem(str(tarea))
            self.titulo_input.clear()
            self.descripcion_input.clear()
            self.hora_limite_input.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios")

    def eliminar_tarea(self):
        current_item = self.list_widget.currentRow()
        if current_item >= 0:
            self.lista_de_tareas.eliminar_tarea(current_item)
            self.list_widget.takeItem(current_item)
        else:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para eliminar")

    def marcar_como_completada(self):
        current_item = self.list_widget.currentRow()
        if current_item >= 0:
            self.lista_de_tareas.marcar_tarea_como_realizada(current_item)
            item = self.list_widget.item(current_item)
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
        else:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para marcar como completada")


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
