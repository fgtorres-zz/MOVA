import Levenshtein as Levenshtein
import lxml as lxml
import nltk
import urllib
import bs4 as bs
import re
from gensim.models import Word2Vec
from nltk.corpus import stopwords

#pega os dados e transforma tudo em uma string
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming')

soup = bs.BeautifulSoup(source, 'lxml')
text = ""
for paragraph in soup.find_all('p'):
    text+= paragraph.text


sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

#faz a remoção de stopwords

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('English')]

model = Word2Vec(sentences, min_count=1)

words = model.wv.vocab

vector = model.wv['global']

# busca a palavra mais similar
similar = model.wv.most_similar('global')
print (similar)