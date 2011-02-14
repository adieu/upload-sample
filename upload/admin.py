from models import UploadModel
from django.contrib import admin
from django.contrib.admin import sites

class AdminSite(sites.AdminSite):
    pass

# TODO - figure out how to set this
# admin.site = AdminSite()

admin.site.register(UploadModel)
