'''
ORMs
'''
import datetime
from peewee import (SqliteDatabase, Model,
                    CharField, DateTimeField,
                    FloatField, PrimaryKeyField,
                    ForeignKeyField, BooleanField,
                    TextField)
from playhouse.fields import ManyToManyField


DATABASE = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = DATABASE


class Sighting(BaseModel):
    '''
    Represents a sighting event of a subject.
    '''
    id = PrimaryKeyField()
    long = FloatField()
    lat = FloatField()
    datetime = DateTimeField(default=datetime.datetime.utcnow)
    confirmed = BooleanField(default=False)


class Subject(BaseModel):
    '''
    Represents a sighted subject
    '''
    id = PrimaryKeyField()
    name = CharField(max_length=36, unique=True)
    bio = TextField(null=True)
    sightings = ManyToManyField(Sighting,
                                related_name='subjects')


class Media(BaseModel):
    """
    Represents multimedia of the sighting event
    """
    id = PrimaryKeyField()
    filename = CharField(unique=True)
    content_type = CharField(null=True)
    url = CharField(unique=True)
    sighting = ForeignKeyField(Sighting,
                               related_name='media_files')


SightingSubject = Subject.sightings.get_through_model()


def init_database(database_name: str) -> None:
    '''
    @description: helper to connect to DB and create
    tables.

    @arg database_name: {str} The URI of the database to
    connect to.
    '''
    DATABASE.init(database_name)
    DATABASE.connect()
    DATABASE.create_tables([Sighting,
                            Subject,
                            SightingSubject,
                            Media])
