file = open("books/alice.txt")

line = file.read().replace("\n", " ")
file.close()

import nltk
# nltk.download('punkt')

from nltk import tokenize

sentences = tokenize.sent_tokenize(line)
for s in sentences:
    print(s)
