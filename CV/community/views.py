from django.shortcuts import render, redirect

from community.forms import PostForm
from community.models import CV

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from eunjeon import Mecab  #은전한잎
tagger = Mecab()
import re
import networkx as nx
from collections import Counter
num_top_nouns = 20

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
        letter = req.POST['letter']  #
        nouns = []
        for word in tagger.nouns(str(letter)):
            if len(word) > 1:
                nouns.append(word)
        counted_nouns = Counter(nouns)
        top_20 = dict(counted_nouns.most_common(num_top_nouns))
        wc = WordCloud(font_path='/static/NanumSquareRoundB.ttf', background_color='white', width=700, height=400)
        # cloud = wc.generate_from_frequencies(top_20) ## 이줄부터 오류 발생
        # plt.figure(figsize=(10,5))
        # plt.imshow(cloud)
        # plt.axis("off")
        # plt.savefig(image, format='png')
        # image.seek(0)
        # wordcloud = word_cloud()
        # cloud.to_file("/static/img/keyword.jpg")
        context = {
            'post': post,
            'top1': list(top_20.keys())[0],
            'top2': list(top_20.keys())[1],
            'top3': list(top_20.keys())[2],
            'top4': list(top_20.keys())[3],
            'top5': list(top_20.keys())[4],
            # 'wordcloud': cloud
        }
        return render(req, 'result.html', context=context)
