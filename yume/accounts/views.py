from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm
from django.contrib import messages

# Create your views here.

class Login(LoginView):
    template_name = "accounts/auth.html"

    def from_valid(self, form):
        messages.success(self.request, 'ログインできました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'エラーです...')
        return super().form_invalid(form)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save
            messages.success(request, '登録できました！')
            return redirect('/')
    return render(request, 'accounts/auth.html', context)


