from program.models import VocabularyBank, Vocabulary
from dictionary.models import Word

vb = VocabularyBank.prefetch_related.create(name="toefl", alias="托福", description="精選3000+托福單字庫")

with open("program/services/programs/toefl.txt", "r") as f:
    for vocab in f:
        vocab = vocab.strip()
        w = Word.objects.get(rep=vocab)
        Vocabulary.objects.create(word=w, bank=vb)


# vocab_list = open("program/services/programs/toefl.txt", "r")
# while True:
#     line = vocab_list.readline().rstrip('\n')
#
#     if not line:
#         break
#
#     token = line.split(', ')
#     level = token[0]
#     vocab = token[1]
#     translation = token[2]
#     # print(vocab)
#
#     try:
#         w = Word.objects.get(rep__iexact=vocab)
#         # print(w.rep)
#         v = Vocabulary.objects.create(rep=vocab, vocabulary_list=vl)
#     except:
#         print(vocab + " not found.")

