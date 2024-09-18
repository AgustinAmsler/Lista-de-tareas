from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Tarea, ListaDeTareas
from PySide6.QtCore import Qt
from main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lista_de_tareas = ListaDeTareas()
        self.ui.agregar_button.clicked.connect(self.agregar_tarea)
        self.ui.eliminar_button.clicked.connect(self.eliminar_tarea)
        self.ui.completar_button.clicked.connect(self.marcar_como_completada)

    def agregar_tarea(self):
        titulo = self.ui.titulo_input.text()
        descripcion = self.ui.descripcion_input.text()
        hora_limite = self.ui.hora_limite_input.text()

        if titulo and descripcion and hora_limite:
            tarea = Tarea(titulo, descripcion, hora_limite)
            self.lista_de_tareas.agregar_tarea(tarea)
            self.ui.listWidget.addItem(str(tarea))
            self.ui.titulo_input.clear()
            self.ui.descripcion_input.clear()
            self.ui.hora_limite_input.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios")

    def eliminar_tarea(self):
        current_item = self.ui.listWidget.currentRow()
        if current_item >= 0:
            self.lista_de_tareas.eliminar_tarea(current_item)
            self.ui.listWidget.takeItem(current_item)
        else:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para eliminar")

    def marcar_como_completada(self):
        current_item = self.ui.listWidget.currentRow()
        if current_item >= 0:
            self.lista_de_tareas.marcar_tarea_como_realizada(current_item)
            item = self.ui.listWidget.item(current_item)
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
            item.setForeground(Qt.gray)
        else:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para marcar como completada")

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
