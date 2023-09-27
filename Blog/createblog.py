from django.views.generic import CreateView
from .models import Post

class CreateBlogView(CreateView):
    model = Post
    template_name = 'createblog.html'
    fields = ['title', 'author', 'content', 'pu_date' ] 
    success_url = '/'  
