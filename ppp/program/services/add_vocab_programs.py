from program.models import VocabularyBank, Vocabulary, VocabularyProgram
from dictionary.models import Word
import random

# value = random()
program_size = 1000
name = "toefl"

vb = VocabularyBank.objects.prefetch_related('vocabularies').get(name=name)
vocabularies = list(vb.vocabularies.all())
count = len(vocabularies)
program_count = int(count / program_size) + 1

random.shuffle(vocabularies)

programs = []
program_size_counts = [0 for i in range(program_count)]

for i in range(program_count):
    program_name = name + "_" + str(i + 1)
    vp = VocabularyProgram.objects.create(name=program_name)
    programs.append(vp)

for program in programs:
    i = 0
    while vocabularies and i != program_size:
        vocabulary = vocabularies.pop()
        vocabulary.vocab_program = program
        vocabulary.save()
        i += 1
