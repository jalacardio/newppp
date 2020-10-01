# relation_txt = open("dictionary/services/book/alice.txt", "r")
import urllib.request
import os
import pathlib

from nltk.stem import WordNetLemmatizer
from dictionary.models import Word, WordAnalysis

urls = ['https://www.gutenberg.org/files/1342/1342-0.txt']


def download(url):
    head, file_name = os.path.split(url)
    file = pathlib.Path("dictionary/services/book/books/" + file_name)
    if file.exists():
        return False
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(url, file)
    return file_name

for url in urls:
    # file_name = download(url)
    file_name = "1661-0.txt"
    if file_name:
        relation_txt = open("dictionary/services/book/books/" + file_name, "r")
        word_count = {}
        while True:
            line = relation_txt.readline()
            if not line:
                break
            words = line.split(' ')
            for word in words:
                if all(c.isalpha() for c in word):
                    if word.lower() in word_count:
                        word_count[word.lower()] += 1
                    else:
                        word_count[word.lower()] = 1
        wnl = WordNetLemmatizer()
        print(len(word_count))
        for word, count in word_count.items():
            print(word)
            w = Word.objects.filter(rep=word).first()
            if not w:
                word = wnl.lemmatize(word, pos='v')
                w = Word.objects.filter(rep=word).first()
            if not w:
                word = wnl.lemmatize(word, pos='n')
                w = Word.objects.filter(rep=word).first()
            if not w:
                continue
            ana, created = WordAnalysis.objects.get_or_create(word=w)
            # print(created)
            ana.total_occurrence = ana.total_occurrence + count
            ana.save()
            print(word, " -> ", count)



