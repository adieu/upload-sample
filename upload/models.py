from django.db import models

class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]
