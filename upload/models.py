from django.db import models

from google.appengine.api.images import get_serving_url

class UploadModel(models.Model):
    title = models.CharField(max_length=64, blank=True)
    file = models.ImageField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    @property
    def image_thumbnail_url(self):
        return get_serving_url(str(self.file.file.blobstore_info.key()), 200)
