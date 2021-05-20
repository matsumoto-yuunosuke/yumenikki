from django import forms
from django.contrib.auth import get_user_model
from .models import DreamModel, IdeaModel


class UserCreationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('email',)
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UploadImgForm(forms.ModelForm):
  class Meta:
    model = DreamModel
    fields = ('title', 'content', 'image_1', 'image_2', 'image_3', 'image_4', 'create_time')

class UploadIdaForm(forms.ModelForm):
  class Meta:
    model = IdeaModel
    fields = ('dream', 'title', 'content', 'image_1', 'image_2', 'image_3', 'image_4', 'create_time')