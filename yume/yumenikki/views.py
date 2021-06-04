from django.views import generic
from django.shortcuts import render, redirect
from .models import DreamModel, IdeaModel, DreamTag
from .forms import UploadImgForm, UploadIdaForm
from django.urls import reverse_lazy
from . import forms

# Create your views here.

def dream_list_view(request):
    ranks = DreamModel.objects.order_by('-count')[:2] # 降順で表示
    objs = DreamModel.objects.all()
    context = {
        'dreams':objs,
        'ranks':ranks,
    }
    return render(request, 'yumenikki/dream_list.html', context)

def dream_detali_view(request, pk):
    obj = DreamModel.objects.get(pk=pk)
    if request.POST.get('like_count', None):
        obj.count += 1
        obj.save()
    
    context = {"dreammodel":obj}
    return render(request, 'yumenikki/dream_detail.html', context)

# class DreamIdeaDetail(generic.DetailView):
#     template_name = 'yumenikki/dream_idea_detail.html'
#     model = DreamModel

class DreamUpdate(generic.UpdateView):
    template_name = 'yumenikki/dream_update.html'
    model = DreamModel
    fields = ('title', 'content', 'image_1', 'image_2', 'image_3', 'image_4')
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
            date = UploadImgForm(request.POST, request.FILES, instance=DreamModel())
            date.save()
            title: str = str(request.POST["title"])
            idea_id: int = DreamModel.objects.filter(title=title)[0].id
            return redirect('dream_detail', pk=idea_id)
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


def idea_upload(request, pk):
    obj = DreamModel.objects.get(pk=pk)
    if request.method == 'POST':
            form = UploadIdaForm(request.POST)
            if form.is_valid():
                idea = form.save(commit=False)
                idea.dream = obj
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
                return redirect('idea_detail', pk=form.pk)
    else:
        form = UploadIdaForm()
    return render(request, 'yumenikki/idea_create.html', {'form': form})

    # if request.method == "POST":
    #     form = UploadIdaForm(request.POST)
    #     if form.is_valid():
    #         idea = IdeaModel()
    #         print(request)
    #         idea.dream = request.POST['dream']
    #         idea.title = request.POST['title']
    #         idea.content = request.POST['content']
    #         idea.create_time = request.POST['create_time']
    #         try:
    #             idea.image_1 = request.FILES['image_1']
    #         except:
    #             pass
    #         try:
    #             idea.image_2 = request.FILES['image_2']
    #         except:
    #             pass
    #         try:
    #             idea.image_3 = request.FILES['image_3']
    #         except:
    #             pass
    #         try:
    #             idea.image_4 = request.FILES['image_4']
    #         except:
    #             pass
    #         idea.save()
    #         return redirect('idea_detail', pk=idea.pk)
    # else:
    #     form = UploadIdaForm()
    # return render(request, 'yumenikki/idea_create.html', {'form': form})

def idea_detali_view(request, pk):
    obj = IdeaModel.objects.get(pk=pk)
    context = {"ideamodel":obj}
    return render(request, 'yumenikki/idea_detail.html', context)

class IdeaDelete(generic.DeleteView):
    template_name = 'yumenikki/idea_delete.html'
    model = IdeaModel

    success_url = reverse_lazy('idea_list')

def tags(request, slug):
    tag = DreamTag.objects.get(slug=slug)
    objs = tag.dreammodel_set.all()
    # ranks = DreamModel.objects.order_by('-count')[:2]

    context = {
        'dreams':objs,
        # 'ranks':ranks,
    }
    return render(request, 'yumenikki/tags_list.html', context)
