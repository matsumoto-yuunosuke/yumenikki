from django.views import generic
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import DreamModel, IdeaModel
from .forms import UploadImgForm, UploadIdaForm
from django.urls import reverse_lazy

# Create your views here.

class DreamList(generic.ListView):
    template_name = 'yumenikki/dream_list.html'
    model = DreamModel

class DreamDetail(generic.DetailView):
    template_name = 'yumenikki/dream_detail.html'
    model = DreamModel

class DreamIdeaDetail(generic.DetailView):
    template_name = 'yumenikki/dream_idea_detail.html'
    model = DreamModel

class DreamUpdate(generic.UpdateView):
    template_name = 'yumenikki/dream_update.html'
    model = DreamModel
    fields = ('title', 'content', 'create_time')
    success_url = reverse_lazy('dream_list')

class DreamDelete(generic.DeleteView):
    template_name = 'yumenikki/dream_delete.html'
    model = DreamModel

    success_url = reverse_lazy('dream_list')

#アップロード
def dream_upload(request):
    if request.method == "POST":
        form = UploadImgForm(request.POST)
        if form.is_valid():
            dream = DreamModel()
            print(request)
            dream.title = request.POST['title']
            dream.content = request.POST['content']
            dream.create_time = request.POST['create_time']
            try:
                dream.image_1 = request.FILES['image_1']
            except:
                pass
            try:
                dream.image_2 = request.FILES['image_2']
            except:
                pass
            try:
                dream.image_3 = request.FILES['image_3']
            except:
                pass
            try:
                dream.image_4 = request.FILES['image_4']
            except:
                pass
            dream.save()
            return redirect('dream_detail', pk=dream.pk)
    else:
        form = UploadImgForm()
    return render(request, 'yumenikki/dream_create.html', {'form': form})

class IdeaList(generic.ListView):
    template_name = 'yumenikki/idea_list.html'
    model = IdeaModel
    context_object_name = 'ideas'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['dreams'] = DreamModel.objects.all
        context['ideas'] = IdeaModel.objects.all
        return context


def idea_upload(request):
    if request.method == "POST":
        form = UploadIdaForm(request.POST)
        if form.is_valid():
            idea = IdeaModel()
            print(request)
            idea.dream = request.POST['dream']
            idea.title = request.POST['title']
            idea.content = request.POST['content']
            idea.create_time = request.POST['create_time']
            try:
                idea.image_1 = request.FILES['image_1']
            except:
                pass
            try:
                idea.image_2 = request.FILES['image_2']
            except:
                pass
            try:
                idea.image_3 = request.FILES['image_3']
            except:
                pass
            try:
                idea.image_4 = request.FILES['image_4']
            except:
                pass
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = UploadIdaForm()
    return render(request, 'yumenikki/idea_create.html', {'form': form})

class IdeaDetail(generic.DetailView):
    template_name = 'yumenikki/idea_detail.html'
    model = IdeaModel

class IdeaDelete(generic.DeleteView):
    template_name = 'yumenikki/idea_delete.html'
    model = IdeaModel

    success_url = reverse_lazy('idea_list')

#ログイン
class Login(LoginView):
    template_name = 'yumenikki/login.html'



