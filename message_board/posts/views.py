#from django.shortcuts import render
#from .models import Post
# Create your views here
#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, "post_list.html", {"posts" : posts})
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post 
    template_name = "post_list.html"        #""" The current template uses a context dictionary called posts. By default, ListView returns acontext variable called <model>_list, where <model> is our model name."""

