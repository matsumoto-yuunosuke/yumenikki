from django import forms
from .models import DreamModel, IdeaModel, DreamTag



class UploadImgForm(forms.ModelForm):
  class Meta:
    model = DreamModel
    fields = ('title', 'content', 'image_1', 'image_2', 'image_3', 'image_4', 'create_time', 'dtags')

class UploadIdaForm(forms.ModelForm):
  class Meta:
    model = IdeaModel
    fields = ('dream', 'title', 'content', 'image_1', 'image_2', 'image_3', 'image_4', 'create_time')