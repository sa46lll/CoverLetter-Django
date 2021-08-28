import base64, io, urllib
from django.shortcuts import render, redirect
from community.forms import PostForm
from community.models import CV

from eunjeon import Mecab  #은전한잎
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

tagger = Mecab()
num_top_nouns = 20


def keyword(text):
    nouns = []
    for word in tagger.nouns(str(text)):
        if len(word) > 1:
            nouns.append(word)
    counted_nouns = Counter(nouns)
    return dict(counted_nouns.most_common(num_top_nouns))


def word_cloud(text):
    wc = WordCloud(font_path='static/img/NanumGothic.ttf', background_color='white', width=300, height=200)
    cloud = wc.generate_from_frequencies(dict(text))
    plt.figure(figsize=(20, 10))
    plt.tight_layout(pad=0)
    plt.imshow(cloud)
    plt.axis("off")
    fig = plt.gcf()
    image = io.BytesIO()
    fig.savefig(image, format='png', bbox_inches='tight')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_64


# Create your views here.
def index(req):
    form = PostForm()
    return render(req, "index.html", {"form": form})


def post_result(req):
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():
            print("form valid")
            post = form.save(commit=False)
            post.ip = req.META['REMOTE_ADDR']
            post.save()
            # return redirect('posts')
        else:
            print("form invalid")
            post = CV.objects.all()

        # 키워드
        letter = req.POST['letter']
        keywords = keyword(letter)
        # 워드 클라우드
        wordcloud = word_cloud(keywords)

        context = {
            'post': post,
            'top1': list(keywords.keys())[0],
            'top2': list(keywords.keys())[1],
            'top3': list(keywords.keys())[2],
            'top4': list(keywords.keys())[3],
            'top5': list(keywords.keys())[4],
            'wordcloud': wordcloud,
        }
        return render(req, 'result.html', context=context)
