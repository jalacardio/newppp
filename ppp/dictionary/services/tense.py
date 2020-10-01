from dictionary.models import Word, Translation

relation_txt = open("dictionary/services/stardict-langdao-ec-big5-2.4.2/relations.txt", "r")

while True:
    line = relation_txt.readline()
    if not line:
        break
    content = line.split(',')
    word = content[0]
    meaning = content[1]
    w, created = Word.objects.get_or_create(rep=word)
    m = Translation.objects.create(rep=meaning, word=w)
    print(w.rep, " -> ", m.rep)

    # relations = content[1]
    # relations = relations.split("的")
    # parent_word = relations[0]
    # tenses = relations[1]
    # tenses = tenses.split("和")
    # try:
    #     pw = Word.objects.get(rep=parent_word)
    # except:
    #     continue
    # w, created = Word.objects.get_or_create(rep=word)
    # # print(pw.rep)
    # for tense in tenses:
    #     print(parent_word, word, tense)
    #     Tense.objects.get_or_create(parent=pw, child=w, rep=tense)
