from __future__ import unicode_literals, absolute_import

import os

from django.conf import settings
from django.db import models
from overwrite_storage.storage import OverwriteStorage


foo_storage = OverwriteStorage(
        location=os.path.join(settings.MEDIA_ROOT,
                              "foos")
)

def gen_foo_file_path(instance, filename):
    return os.path.join(foo_storage.location,
                        str(instance.id),
                        filename)


class Foo(models.Model):
    doc = models.FileField(upload_to=gen_foo_file_path,
                           storage=foo_storage)

class BarStorage(OverwriteStorage):
    location = os.path.join(settings.MEDIA_ROOT, "bars")


bar_storage = BarStorage()


def gen_bar_file_path(instance, filename):
    return os.path.join(bar_storage.location, filename)


class Bar(models.Model):
    doc = models.FileField(upload_to=gen_bar_file_path,
                           storage=bar_storage)


def gen_baz_file_path(instance, filename):
    # print vars(instance)
    return os.path.join(settings.MEDIA_ROOT,
                        instance.__class__._meta.verbose_name_plural,
                        filename)


class Baz(models.Model):
    doc = models.FileField(upload_to=gen_baz_file_path,
                           storage=OverwriteStorage())


    class Meta:
        verbose_name_plural = "bazzes"


class BooStorage(OverwriteStorage):
    location = os.path.join(settings.MEDIA_ROOT, "boos")

    @classmethod
    def gen_file_path(cls, instance, filename):
        return os.path.join(cls.location, filename)

boo_storage = BooStorage()


class Boo(models.Model):
    doc = models.FileField(upload_to=boo_storage.gen_file_path,
                           storage=boo_storage)


def gen_quux_file_path(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, "images", filename)


class Quux(models.Model):
    image = models.ImageField(upload_to=gen_quux_file_path,
                              storage=OverwriteStorage())
