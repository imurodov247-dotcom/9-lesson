from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    
    maqolalar = Post.objects.all()
    return render(request,"blog/index.html",{"maqolalar":maqolalar})

def maqola(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,"blog/maqola.html",{"post":post })