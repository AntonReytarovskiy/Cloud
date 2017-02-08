import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.context_processors.user_memory import memory
from app.forms import UploadForm


def default(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('catalog'))
    else:
        return render(request, 'welcome.html')

@login_required(login_url='/user/login')
def catalog(request):
    dir = os.path.join('app/media', request.user.username)
    files = []
    for entry in os.scandir(path=dir):
        files.append(entry)

    return render(request, 'catalog.html', {'files': files})

@login_required(login_url='/user/login')
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.max_size = memory(request).get('free_size')
        if form.is_valid():
            try:
                UploadForm.upload(form, request.FILES['file'], request.user.username)
                return HttpResponseRedirect(reverse('catalog'))
            except FileExistsError:
                return render(request, 'fileError.html')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/user/login')
def download(request, filename):
    try:
        dir = os.path.join('app/media', request.user.username)
        file = open(os.path.join(dir, filename), 'rb')
        return HttpResponse(file, content_type='application/octet-stream')
    except FileNotFoundError:
        return render(request, 'FileNotFound.html')

@login_required(login_url='/user/login')
def remove(request, filename):
    try:
        dir = os.path.join('app/media', request.user.username)
        os.remove(os.path.join(dir, filename))
        return HttpResponseRedirect(reverse('catalog'))
    except FileNotFoundError:
        return render(request, 'FileNotFound.html')