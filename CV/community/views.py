from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
#def index(req):
#    context = {
#
#    }
#    return render(req, "index.html", context=context)

def post(request):
    if request.method=='POST':
        post=Post()
        post.letter=request.POST['letter']
        post.job = request.POST['job']
        post.save()
        return redirect('post')
    else:
        post=Post.objects.all()
        return render(request, 'index.html', {'post':post})