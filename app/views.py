from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app.forms import UploadForm


def default(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('catalog'))
    else:
        return render(request, 'welcome.html')

@login_required(login_url='/user/login')
def catalog(request):
    return render(request, 'catalog.html')

@login_required(login_url='/user/login')
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                path = UploadForm.upload(form, request.FILES['file'], request.user.username)
            except FileExistsError:
                return render(request, 'fileError.html')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'input': form['file']})