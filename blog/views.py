from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Entry


class EntryListView(ListView):
    model = Entry
    context_object_name = 'blog_entries'

    # def get_queryset(self, show=True):
    #     return Entry.objects.filter(is_active=show)


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class EntryCreateView(CreateView):
    model = Entry
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('blog:entry_list')
    context_object_name = 'entry'


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['title', 'content', 'preview', 'is_active']
    success_url = reverse_lazy('blog:entry_detail')
    template_name = 'blog/entry_form.html'
    context_object_name = 'entry'


class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'blog/entry_delete.html'
    success_url = reverse_lazy('blog:entry_list')
