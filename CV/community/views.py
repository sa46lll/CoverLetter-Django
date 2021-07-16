from django.http import request
from django.shortcuts import redirect, render


# Create your views here.
def index(req):
    context = {

    }
    return render(req, "index.html", context=context)


def Post(req):
    if req.method == 'POST':
        post = Post()
        post.letter = request.POST['letter']
        post.job = request.POST['job']
        post.save()
        return redirect('post')
    else:
        post = Post.objects.all()
        return render(req, 'result.html', {"post": post})
