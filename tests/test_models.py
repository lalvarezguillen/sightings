from sightings import models

def test_create_individuo():
    fulano = models.Individuo(nombre='Fulano')
    assert models.Individuo.count() == 1