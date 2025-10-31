from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.shortcuts import get_object_or_404 , render
from django.urls  import reverse_lazy
# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = "blogpost_list.html"

#def post_detail(request, pk):
 #   post = get_object_or_404(BlogPost, pk=pk)
  #  return render(request,"post_detail.html",{"post":post})

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"
    context_object_name = "detailpost"

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "post_create_form.html"
    fields = ["title", "body", "author"]

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = "post_update.html"
    fields = ["title","body"]

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")