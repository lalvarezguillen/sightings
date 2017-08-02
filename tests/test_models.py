'''
Unittests for the ORMs
'''
from sightings.models import (Sighting,
                              Subject,
                              Media,
                              init_database)


class TestModels:
    @classmethod
    def setup_class(cls):
        init_database(':memory:')

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
        in_caracas.subjects = [luis, rita]
        in_caracas.save()
        luis.update()
        assert len(luis.sightings) == 1

    def test_media_creation(self):
        in_caracas = Sighting.get(Sighting.lat == 80.08)
        picture = Media(filename='test.file',
                        content_type='application/unknown',
                        url='www.test_file.com',
                        sighting=in_caracas)
        picture.save()
        in_caracas.update()
        assert in_caracas.media_files[0].id == picture.id
