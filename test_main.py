import pytest
from main import Tarea, Lista_de_tareas


def test_crear_tarea():

    tarea = Tarea("Hacer la cama", "Hacer la cama despues de despertarme", "08:00:00")
    assert tarea.comprobar_titulo("Hacer la cama")
    assert tarea.comprobar_descripcion("Hacer la cama despues de despertarme")
    assert tarea.comprobar_hora_limite("08:00:00")


def test_agregar_1_tarea_a_una_lista_de_tareas():
        
    lista_de_tareas = Lista_de_tareas()
    tarea = Tarea("Hacer la cama", "Hacer la cama despues de despertarme", "08:00:00")
    lista_de_tareas.agregar_tarea(tarea)
    assert lista_de_tareas.comprobar_cantidad_de_tareas(1)

