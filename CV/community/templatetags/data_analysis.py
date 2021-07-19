from django import template
register = template.Library()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from eunjeon import Mecab  #은전한잎
tagger = Mecab()
import re
import networkx as nx
from collections import Counter
num_top_nouns = 20

def make_wordcloud(letter):
    nouns = []
    for word in tagger.nouns(str(letter)):
        if len(word) > 1:
            nouns.append(word)
    counted_nouns = Counter(nouns)
    top_20 = dict(counted_nouns.most_common(num_top_nouns))
    wc = WordCloud(font_path='/static/NanumSquareRoundB.ttf', background_color='white', width=700, height=400)
    cloud = wc.generate_from_frequencies(top_20)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    return plt.show()

def top_1(letter):
    nouns = []
    for word in tagger.nouns(str(letter)):
        if len(word) > 1:
            nouns.append(word)
    counted_nouns = Counter(nouns)
    top_20 = dict(counted_nouns.most_common(num_top_nouns))
    # context = { "top1":list(top_20.keys())[0]}
    # return HttpResponse(template.render(context,req))
    return list(top_20.keys())[0]