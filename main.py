class Tarea:
    def __init__(self, titulo, descripcion, hora_limite):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__hora_limite = hora_limite

    def comprobar_titulo(self, titulo):
        return self.__titulo == titulo

    def comprobar_descripcion(self, descripcion):
        return self.__descripcion == descripcion

    def comprobar_hora_limite(self, hora_limite):
        return self.__hora_limite == hora_limite


class Lista_de_tareas:
    def __init__(self):
        self.__lista_de_tareas = []

    def agregar_tarea(self, tarea):
        self.__lista_de_tareas.append(tarea)

    def comprobar_cantidad_de_tareas(self, numero):
        return len(self.__lista_de_tareas) == numero

