from dictionary.models import Word

with open("program/services/programs/toefl.txt", "r") as f:
    for vocab in f:
        vocab = vocab.strip()
        w = Word.objects.filter(rep=vocab)
        if w:
            pass
            # print("Good!" + vocab)
        else:
            print(vocab)
