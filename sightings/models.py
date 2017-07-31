'''
ORMs
'''
from uuid import uuid4
from peewee import (SqliteDatabase, Model, CharField,
                    FloatField, PrimaryKeyField)
from playhouse.fields import ManyToManyField


DATABASE = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = DATABASE


class Sighting(BaseModel):
    '''
    Representa eventos de Sighting de Subjects
    '''
    id = PrimaryKeyField(null=False)
    long = FloatField(null=False)
    lat = FloatField(null=False)


class Subject(BaseModel):
    '''
    Representa un Subject avistado
    '''
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=36, null=False,
                     unique=True)
    sightings = ManyToManyField(Sighting,
                                related_name='subjects')


SightingSubject = Subject.sightings.get_through_model()


def init_database(database_name):
    DATABASE.init(database_name)
    DATABASE.connect()
    DATABASE.create_tables([Sighting,
                            Subject,
                            SightingSubject])
