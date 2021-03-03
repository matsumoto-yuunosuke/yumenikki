from django.views import generic
from .models import DreamModel, IdeaModel
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
    success_url = reverse_lazy('list')

class DreamDelete(generic.DeleteView):
    template_name = 'yumenikki/dream_delete.html'
    model = DreamModel

    success_url = reverse_lazy('list')

class DreamCreate(generic.CreateView):
    template_name = 'yumenikki/dream_create.html'
    model = DreamModel
    fields = ('title', 'content', 'create_time')

    success_url = reverse_lazy('list')

class IdeaList(generic.ListView):
    template_name = 'yumenikki/idea_list.html'
    model = IdeaModel
    context_object_name = 'ideas'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['dreams'] = DreamModel.objects.all
        context['ideas'] = IdeaModel.objects.all
        return context


class IdeaCreate(generic.CreateView):
    template_name = 'yumenikki/idea_create.html'
    model = IdeaModel
    fields = ('title', 'content', 'create_time', 'dream')

    success_url = reverse_lazy('idea_list')

class IdeaDetail(generic.DetailView):
    template_name = 'yumenikki/idea_detail.html'
    model = IdeaModel



