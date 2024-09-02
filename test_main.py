import pytest
from main import Tarea


def test_crear_tarea():

    tarea = Tarea("Hacer la cama", "Hacer la cama despues de despertarme", "08:00:00")
    assert tarea.comprobar_titulo("Hacer la cama")
    assert tarea.comprobar_descripcion("Hacer la cama despues de despertarme")
    assert tarea.comprobar_hora_limite("08:00:00")
