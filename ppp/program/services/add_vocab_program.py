from program.models import VocabularyProgram, VocabularyList, Vocabulary
from dictionary.models import Word


vocab_list = open("dictionary/services/book/gept/easy.txt", "r")

vp = VocabularyProgram.objects.create(name="gept_easy", alias="全民英檢初級", description="精選2000+全民英檢初級單字庫")
vl = VocabularyList.objects.create(program=vp)


while True:
    line = vocab_list.readline().rstrip('\n')

    if not line:
        break

    token = line.split(', ')
    level = token[0]
    vocab = token[1]
    translation = token[2]
    # print(vocab)

    try:
        w = Word.objects.get(rep__iexact=vocab)
        # print(w.rep)
        v = Vocabulary.objects.create(rep=vocab, vocabulary_list=vl)
    except:
        print(vocab + " not found.")

