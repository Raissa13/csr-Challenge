from django.urls import path
from .views import HomeView, CreateBlogView, IndexView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),  
    path('createblog/', CreateBlogView.as_view(), name='create_blog'), 
    path('index/', IndexView.as_view(), name="index"), 
]