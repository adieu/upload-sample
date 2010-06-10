from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from upload.forms import StorageForm
from upload.models import StorageModel

from djangotoolbox.storage import prepare_upload, serve_file

def upload_handler(request):
    if request.method == 'POST':
        form = StorageForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')
    form = StorageForm()
    upload_url, upload_data = prepare_upload('/')
    return direct_to_template(request, 'upload/upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data,
         'files': StorageModel.objects.all()})

def download_handler(request, pk):
    file = get_object_or_404(StorageModel, pk=pk).file
    return serve_file(request, file, save_as=True)

def delete_handler(request, pk):
    get_object_or_404(StorageModel, pk=pk).delete()
    return HttpResponseRedirect('/')
