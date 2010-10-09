import os
import shutil

from django.conf import settings
from django.core.files import File
from django.test import TestCase

from hort.utils.iterators import make_iterable, section, chunk

from models import Album


class DbFieldsTestCase(TestCase):

    def setUp(self):
        os.mkdir(settings.MEDIA_ROOT)

    def tearDown(self):
        shutil.rmtree(settings.MEDIA_ROOT)

    def test_post_save_field(self):
        with open(os.path.join(settings.ASSET_ROOT, 'test.jpg')) as fp:
            album = Album(title='hello world', cover=File(fp, 'test.jpg'))
            album.save()
            self.assertEquals(os.listdir(settings.MEDIA_ROOT), ['album-1.jpg'])


class UtilsTestCase(TestCase):

    def test_make_iterable(self):
        result = list(make_iterable('foo', ['bar', 'baz'], ['hello', 'world']))
        expected = ['foo', 'bar', 'baz', 'hello', 'world']
        self.assertEquals(result, expected)

    def test_section(self):
        people = ['Dustin', 'Sean', 'Steve', 'Eliana', 'Megan']
        result = list(section(people, 2))
        expected = [['Dustin', 'Sean'], ['Steve', 'Eliana'], ['Megan']]
        self.assertEquals(result, expected)

    def test_chunk(self):
        people = ['Dustin', 'Sean', 'Steve', 'Eliana', 'Megan']
        result = list(chunk(people, 2))
        expected = [['Dustin', 'Sean', 'Steve'], ['Eliana', 'Megan']]
        self.assertEquals(result, expected)

