from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Entry
from django.urls import reverse_lazy


class EntryListView(ListView):
    model = Entry
    context_object_name = 'blog_entries'

    def get_queryset(self, show=True):
        return Entry.objects.filter(is_active=show)


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'blog_entry'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class EntryCreateView(CreateView):
    model = Entry
    fields = ['title', 'content', 'preview', 'is_active']
    success_url = reverse_lazy('blog:entry_list')


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['title', 'content', 'preview', 'is_active']
    success_url = reverse_lazy('blog:entry_detail')
    template_name = 'blog/entry_form.html'


class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'blog/entry_delete.html'
    success_url = reverse_lazy('blog:entry_list')
