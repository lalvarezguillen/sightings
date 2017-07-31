'''
Unittests for the ORMs
'''
import os
from peewee import SqliteDatabase
from sightings.models import (Sighting, Subject,
                              SightingSubject,
                              DATABASE)


class TestModels:
    @classmethod
    def setup_class(cls):
        DATABASE.init('test.db')
        DATABASE.connect()
        DATABASE.create_tables([Sighting,
                                Subject,
                                SightingSubject])

    def test_subject_creation(self):
        rita = Subject(name='Rita')
        rita.save()
        luis = Subject(name='Luis')
        luis.save()
        assert Subject.select().count() == 2

    def test_sighting_creation(self):
        in_caracas = Sighting(lat=80.08,
                              long=99.99)
        in_caracas.save()

        luis = Subject.get(Subject.name == 'Luis')
        rita = Subject.get(Subject.name == 'Rita')
        in_caracas.individuos = [luis, rita]
        in_caracas.save()
        assert len(list(in_caracas.individuos)) == 2

    @classmethod
    def teardown_class(cls):
        os.remove('test.db')
