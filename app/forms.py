import os

from django import forms
from django.core.exceptions import ValidationError


class UploadForm(forms.Form):
    max_size = 0

    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'hidden'}))

    def upload(self, file, username):
        dir = os.path.join('app/media/', username)
        path = os.path.join(dir, file.name)
        self.checkFile(path)
        with open(path, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

    def checkFile(self, path):
        if os.path.exists(path):
            raise FileExistsError()

    def clean(self):
        if self.cleaned_data.get('file')._size > self.max_size:
            raise ValidationError('Not enough memory', code='Invalid')