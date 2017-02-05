from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def default(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('catalog'))
    else:
        return render(request, 'welcome.html')

@login_required(login_url='/user/login')
def catalog(request):
    return render(request, 'catalog.html')


def upload(request):
    return render(request, 'upload.html')