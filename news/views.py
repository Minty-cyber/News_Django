from django. views. generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from.models import News

class NewsListView(ListView):
    model= News
    template_name = 'news_list.html'

class NewsDetailView(DetailView):
    model= News
    template_name = 'news_detail.html'

class NewsUpdateView(UpdateView):
    model= News
    fields= ('title', 'body',)
    template_name = 'news_edit.html'

class NewsDeleteView(DeleteView):
    model= News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class NewsCreateView(CreateView):
    model= News
    template_name = 'news_create.html'
    fields = ('title', 'body', 'author')
