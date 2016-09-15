import os

from django.core.files import File
from django.core.files.base import ContentFile
from django.test import TestCase

from . import models

class TestOverwriteStorage(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.text_file1 = "tests/data/text_file1.txt"
        self.text_file2 = "tests/data/text_file2.txt"
        self.png_file1 = "tests/data/dark_orange.png"
        self.png_file2 = "tests/data/dark_green.png"

    def tearDown(self):
        pass

    def get_file_name(self, file_path):
        return os.path.basename(file_path)

    def get_bogus_file_upload(self, file_path, file_name=None):
        if file_name is None:
            file_name = os.path.basename(file_path)
        return File(open(file_path, "rb"), name=file_name)

    def test_foo(self):
        foo = models.Foo()
        foo.save()
        foo.doc = self.get_bogus_file_upload(self.text_file1)
        foo.save()
        expected_path = \
            models.gen_foo_file_path(foo,
                                     self.get_file_name(self.text_file1))
        self.assertEqual(foo.doc.name, expected_path)
        expected_content = open(self.text_file1, "rb").read()
        self.assertEqual(foo.doc.read(), expected_content)
        # read in text_file2 but save the name as text_file1
        foo.doc = self.get_bogus_file_upload(
            self.text_file2,
            file_name=self.get_file_name(self.text_file1)
        )
        foo.save()
        # foo.doc should still have now have text_file1's name but be
        # clobbered text_file2's content
        expected_path = models.gen_foo_file_path(foo,
                                                 self.get_file_name(self.text_file1))
        self.assertEqual(foo.doc.name, expected_path)
        expected_content = open(self.text_file2, "rb").read()
        self.assertEqual(foo.doc.read(), expected_content)


    def test_bar(self):
        bar = models.Bar(doc=self.get_bogus_file_upload(self.text_file1))
        bar.save()
        expected_path = \
            models.gen_bar_file_path(bar,
                                    self.get_file_name(self.text_file1))
        self.assertEqual(bar.doc.name, expected_path)
        expected_content = open(self.text_file1, "rb").read()
        self.assertEqual(bar.doc.read(), expected_content)

        # read in text_file2 but save the name as text_file1
        bar.doc = self.get_bogus_file_upload(
            self.text_file2,
            file_name=self.get_file_name(self.text_file1)
        )
        bar.save()
        # foo.doc should still have now have text_file1's name but be
        # clobbered text_file2's content
        expected_path = models.gen_bar_file_path(bar,
                                                 self.get_file_name(self.text_file1))
        self.assertEqual(bar.doc.name, expected_path)
        expected_content = open(self.text_file2, "rb").read()
        self.assertEqual(bar.doc.read(), expected_content)
        # print baz_inst.doc.name


    def test_baz(self):
        baz = models.Baz(doc=self.get_bogus_file_upload(self.text_file1))
        baz.save()
        expected_path = \
            models.gen_baz_file_path(baz,
                                    self.get_file_name(self.text_file1))
        self.assertEqual(baz.doc.name, expected_path)
        expected_content = open(self.text_file1, "rb").read()
        self.assertEqual(baz.doc.read(), expected_content)

        # read in text_file2 but save the name as text_file1
        baz.doc = self.get_bogus_file_upload(
            self.text_file2,
            file_name=self.get_file_name(self.text_file1)
        )
        baz.save()
        # foo.doc should still have now have text_file1's name but be
        # clobbered text_file2's content
        expected_path = models.gen_baz_file_path(baz,
                                                 self.get_file_name(self.text_file1))
        self.assertEqual(baz.doc.name, expected_path)
        expected_content = open(self.text_file2, "rb").read()
        self.assertEqual(baz.doc.read(), expected_content)
        # print baz_inst.doc.name



    def test_boo(self):
        boo = models.Boo(doc=self.get_bogus_file_upload(self.text_file1))
        boo.save()
        expected_path = \
            models.boo_storage.gen_file_path(boo,
                                             self.get_file_name(self.text_file1))
        self.assertEqual(boo.doc.name, expected_path)
        expected_content = open(self.text_file1, "rb").read()
        self.assertEqual(boo.doc.read(), expected_content)

        # read in text_file2 but save the name as text_file1
        boo.doc = self.get_bogus_file_upload(
            self.text_file2,
            file_name=self.get_file_name(self.text_file1)
        )
        boo.save()
        # foo.doc should still have now have text_file1's name but be
        # clobbered text_file2's content
        expected_path = models.boo_storage.gen_file_path(boo,
                                                 self.get_file_name(self.text_file1))
        self.assertEqual(boo.doc.name, expected_path)
        expected_content = open(self.text_file2, "rb").read()
        self.assertEqual(boo.doc.read(), expected_content)
        # print baz_inst.doc.name


    def test_quux(self):
        quux = models.Quux(image=self.get_bogus_file_upload(self.png_file1))
        quux.save()
        expected_path = \
            models.gen_quux_file_path(quux,
                                      self.get_file_name(self.png_file1))
        self.assertEqual(quux.image.name, expected_path)
        expected_content = open(self.png_file1, "rb").read()
        self.assertEqual(quux.image.read(), expected_content)
        # read in png_file2 but save the name as png_file1
        quux.image = self.get_bogus_file_upload(
            self.png_file2,
            file_name=self.get_file_name(self.png_file1)
        )
        quux.save()
        # quux.image should still have now have png_file1's name but be
        # clobbered png_file2's content
        expected_path = models.gen_quux_file_path(quux,
                                                  self.get_file_name(self.png_file1))
        self.assertEqual(quux.image.name, expected_path)
        expected_content = open(self.png_file2, "rb").read()
        self.assertEqual(quux.image.read(), expected_content)

