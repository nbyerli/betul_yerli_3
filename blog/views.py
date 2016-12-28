from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.forms import BlogEntryForm
from blog.models import BlogEntry


class EntryDetailView(DetailView):
    model=BlogEntry

class EntryListView(ListView):
    model=BlogEntry

class EntryCreateView(CreateView):
    template_name = "blog/blogentry_form.html"
    form_class=BlogEntryForm
    def get_success_url(self):
        return reverse('bloglist')