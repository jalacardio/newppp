from django.db.models import Max
import random
from program.models import VocabularyProgram, FlashCard, Vocabulary, ProgramEnrollment, VocabularyUnderstanding
from dictionary.models import Word
from member.models import Member

from django.db.models import Q, Count


DEFAULT_LEARNING_CURVE_COUNT = 50


class VocabularyProgramService():
    def __init__(self, program_id, user_id):
        self.program = VocabularyProgram.objects.get(id=program_id)
        self.member = Member.objects.get(user__id=user_id)
        pass

    def is_enrolled(self):
        if ProgramEnrollment.objects.filter(member=self.member, vocabulary_program=self.program).exists():
            return True
        else:
            return False

    def enroll(self):
        if self.is_enrolled():
            return True
        else:
            ProgramEnrollment.objects.create(member=self.member, vocabulary_program=self.program)
        return True

    def get_flash_card(self):
        flashcard = FlashCard.objects.filter(vocabulary_program=self.program, member=self.member)
        if flashcard:
            return flashcard.last()
        return None

    def init_flash_card(self):
        flashcard = FlashCard.objects.create(vocabulary_program=self.program, member=self.member)
        rand_vocab_list = self.random_vocabularies(DEFAULT_LEARNING_CURVE_COUNT)
        flashcard.vocabularies.add(*rand_vocab_list)
        return flashcard

    def random_vocabularies(self, count):
        max_id = Vocabulary.objects.filter(vocabulary_list__program=self.program).all().aggregate(max_id=Max("id"))['max_id']
        valid_vocabs = 0
        rand_vocab_list = []

        while valid_vocabs < count:
            pk = random.randint(1, max_id)
            rand_vocab = Vocabulary.objects.filter(pk=pk).first()

            if rand_vocab:
                rand_vocab_list.append(rand_vocab)
                valid_vocabs += 1

        return rand_vocab_list

    def get_random_vocabulary_from_flashcard(self, flashcard_id):
        max_id = Vocabulary.objects.filter(flash_card__id=flashcard_id).all().aggregate(max_id=Max("id"))[
            'max_id']

        while True:
            pk = random.randint(1, max_id)
            vocab = Vocabulary.objects.filter(pk=pk).first()

            if vocab:
                understanding, created = VocabularyUnderstanding.objects.get_or_create(member=self.member, vocabulary=vocab)
                translation = self.get_translation(vocab.rep)
                return vocab, understanding, translation

    def get_vocabulary_understanding(self, vocab_id):
        vu = VocabularyUnderstanding.objects.get(member=self.member, vocabulary__id=vocab_id)
        return vu

    def update_vocabulary_understanding(self, vocab_id, score):
        vu = VocabularyUnderstanding.objects.get(member=self.member, vocabulary__id=vocab_id)
        vu.score += score
        if 0 <= vu.score < 6:
            vu.save()

    def get_translation(self, vocab):
        vocab_obj = Word.objects.prefetch_related('translations', 'phonetic', 'translations__speeches').get(rep=vocab)

        return vocab_obj

    def overall_progress(self):
        # VocabularyUnderstanding.objects.filter(member=self.member, vocabulary__vocabulary_list__program=self.program)
        learnt = Count('vocabulary_understandings', filter=(Q(vocabulary_understandings__score=5) & Q(vocabulary_understandings__vocabulary__vocabulary_list__program=self.program)))
        know = Count('vocabulary_understandings', filter=((Q(vocabulary_understandings__score__gt=0) & Q(vocabulary_understandings__score__lte=5)) & Q(vocabulary_understandings__vocabulary__vocabulary_list__program=self.program)))
        total = self.program.vocabulary_list.vocabularies.count()
        mem = Member.objects.filter(pk=self.member.pk).annotate(learnt=learnt).annotate(know=know)
        progress = {'learnt': mem[0].learnt, 'know': mem[0].know, 'total': total}
        print(progress)
        return progress
