from django.http import HttpResponse
from django.shortcuts import render
from community.forms import *


# Create your views here.
def index(req):
    form = Form()
    # context = {

    # }
    # return render(req, "index.html", context=context)
    return render(req, "index.html", {'form':form})

def result(req):
    context = {

    }
    return render(req, "result.html", context=context)


