class Tarea:
    def __init__(self, titulo, descripcion, hora_limite):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__hora_limite = hora_limite
        self.__tarea_realizada = False

    def comprobar_titulo(self, titulo):
        return self.__titulo == titulo

    def comprobar_descripcion(self, descripcion):
        return self.__descripcion == descripcion

    def comprobar_hora_limite(self, hora_limite):
        return self.__hora_limite == hora_limite

    def marcar_tarea_como_realizada(self):
        self.__tarea_realizada = True

    def comprobar_tarea_realizada(self):
        return self.__tarea_realizada == True

    def __str__(self):
        return f"{self.__titulo} - {self.__descripcion} (Hora límite: {self.__hora_limite})"


class ListaDeTareas:
    def __init__(self):
        self.__lista_de_tareas = []

    def agregar_tarea(self, tarea):
        self.__lista_de_tareas.append(tarea)

    def comprobar_cantidad_de_tareas(self, numero):
        return len(self.__lista_de_tareas) == numero

    def eliminar_tarea(self, tarea):
        if tarea in self.__lista_de_tareas:
            self.__lista_de_tareas.remove(tarea)

    def comprobar_lista_de_tareas_contiene_tarea(self, tarea):
        return tarea in self.__lista_de_tareas

    def marcar_tarea_como_realizada(self, tarea):
        if tarea in self.__lista_de_tareas:
            tarea.marcar_tarea_como_realizada()

    def comprobar_tarea_realizada(self, tarea):
        if tarea in self.__lista_de_tareas:
            return tarea.comprobar_tarea_realizada()
        return False
