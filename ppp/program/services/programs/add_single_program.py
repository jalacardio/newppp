from program.models import Vocabulary, VocabularyProgram, VocabularyTranslation
from dictionary.models import Word
import random

# value = random()

name = "toefl2"
program_name = "Toefl2"

vp = VocabularyProgram.objects.create(name=program_name)

with open("program/services/programs/toefl.txt", "r") as f:
    for vocab in f:
        vocab = vocab.strip()
        w = Word.objects.prefetch_related('translations', 'translations__speeches').get(rep=vocab)
        v = Vocabulary.objects.create(vocab_program=vp, rep=vocab)
        first_translation = w.translations.first()
        speech = first_translation.speeches.first()
        vt = VocabularyTranslation.objects.create(rep=first_translation.rep, speech=speech, vocabulary=v)
        print('{} - {} - {}'.format(vt.vocabulary.rep, vt.rep, vt.speech))

# vb = VocabularyBank.objects.prefetch_related('vocabularies', 'vocabularies__word', 'vocabularies__word__translations', 'vocabularies__word__translations__speeches').get(name=name)

#
# vocabularies = list(vb.vocabularies.all())

# for vocabulary in vocabularies:
#     vocabulary = vocabularies.pop()
#     vocabulary.vocab_program = vp
#     vocabulary.save()
#     first_translation = vocabulary.word.translations.first()
#     speech = first_translation.speeches.first()
#     vt = VocabularyTranslation.objects.create(rep=first_translation.rep, speech=speech, vocabulary=vocabulary)
#     print('{} - {} - {}'.format(vt.vocabulary.word.rep, vt.rep, vt.speech))


