from django.shortcuts import render, redirect

from community.forms import PostForm
from community.models import CV


# Create your views here.
def index(req):
    form = PostForm()

    return render(req, "index.html", {"form": form})


def post_result(req):
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = req.META['REMOTE_ADDR']
            post.save()
            # return redirect('posts')
        else:
            post = CV.objects.all()
        context = {
            'post': post
        }
        return render(req, 'result.html', context=context)
