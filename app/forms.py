import os

from django import forms


class UploadForm(forms.Form):
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