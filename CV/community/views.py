
from django.shortcuts import redirect, render

from community.forms import CVForm
from community.models import CV

# Create your views here.


def index(req):
    form = CVForm()

    return render(req, "index.html", {"form": form})

# def result(req):
#     if if req.method == 'POST':


def post_result(req):
    if req.method == 'POST':
        form = CVForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = req.META['REMOTE_ADDR']
            post.save()
            # return redirect('posts:index')
        else:
            # form = Form()
            post = CV.objects.all()
        context = {
            'post': post
        }
        post = CV.objects.all()
        return render(req, 'result.html', context=context)
        # return redirect('posts:result')
