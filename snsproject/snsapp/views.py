from .forms import PostForm
from .models import Post
from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.

def home(request):
    posts=Post.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts})

def detail(request,post_id):
    post_detail=get_object_or_404(Post,pk=post_id)
    return render(request,'detail.html',{'post_detail':post_detail})

def postcreate(request):
    if request.method=='POST' or request.method=='FILES':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostForm
    return render(request,'post_form.html',{'form':form})    