from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from upload.forms import UploadForm
from upload.models import UploadModel

from filetransfers.api import prepare_upload, serve_file

def upload_handler(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')

    upload_url, upload_data = prepare_upload(request, '/')
    form = UploadForm()
    return direct_to_template(request, 'upload/upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data,
         'files': UploadModel.objects.all()})

def download_handler(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.file, save_as=True)

def delete_handler(request, pk):
    get_object_or_404(UploadModel, pk=pk).delete()
    return HttpResponseRedirect('/')