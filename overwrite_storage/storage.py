from django.core.files.storage import FileSystemStorage
# from django.conf import settings
import os


class OverwriteStorage(FileSystemStorage):
    """Subclass of FileSystemStorage which clobbers existing file"""

    # def __init__(self, *args, **kwargs):
    #     """defaults to self.MEDIA_ROOT if location is not passed in"""
    #     self.location = kwargs.pop("location", settings.MEDIA_ROOT)
    #     super(OverwriteStorage, self).__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        """deletes pre-existing file with same name

        preventing filename mangling"""
        if self.exists(name):
            os.remove(os.path.join(self.location, name))
        return name
