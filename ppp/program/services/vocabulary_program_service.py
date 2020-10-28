from django.db.models import Max, Q, Prefetch
from django.utils import timezone
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
        else:
            flashcard = self.init_flash_card()
            return flashcard

    def init_flash_card(self):
        flashcard = FlashCard.objects.create(vocabulary_program=self.program, member=self.member)
        rand_vocab_list = self.random_vocabularies(DEFAULT_LEARNING_CURVE_COUNT)
        flashcard.vocabularies.add(*rand_vocab_list)
        return flashcard

    def refresh_flash_card(self):
        flashcard = FlashCard.objects.filter(vocabulary_program=self.program, member=self.member)
        rand_vocab_list = self.random_vocabularies(DEFAULT_LEARNING_CURVE_COUNT, new=True)
        flashcard.vocabularies.set(*rand_vocab_list, clear=True)
        return flashcard

    def random_vocabularies(self, count, new=False):
        if new:
            vocab_list = list(self.program.vocabularies.exclude(understandings__score__gt=5).all())
        else:
            vocab_list = list(self.program.vocabularies.all())
        random.shuffle(vocab_list)

        rand_vocab_list = vocab_list[:count]

        return rand_vocab_list

    def get_vocabulary_from_flashcard(self, flashcard_id):
        fc = FlashCard.objects.prefetch_related('vocabularies', 'vocabularies__word',
                                                'vocabularies__word__translations', 'vocabularies__word__phonetic',
                                                'vocabularies__word__translations__speeches').get(pk=flashcard_id)
        vocab_list = list(fc.vocabularies.all())
        random.shuffle(vocab_list)
        vocab = vocab_list[0]
        if vocab:
            understanding, created = VocabularyUnderstanding.objects.get_or_create(member=self.member,
                                                                                   vocabulary_id=vocab.id)
            return vocab, understanding

    def get_vocabulary_understanding(self, vocab_id):
        vu = VocabularyUnderstanding.objects.get(member=self.member, vocabulary__id=vocab_id)
        return vu

    def get_recent_mastered_vocabulary(self, vocab_count):
        learned = (Q(score__gt=4) & Q(vocabulary__vocab_program=self.program))
        mem = Member.objects.prefetch_related(
                Prefetch('understandings', queryset=VocabularyUnderstanding.objects.filter(learned))
                ).get(pk=self.member.pk)
        vocab_learned = mem.understandings.order_by('-mastered_at').all()
        return vocab_learned

    def update_vocabulary_understanding(self, vocab_id, score):
        vu = VocabularyUnderstanding.objects.get(member=self.member, vocabulary__id=vocab_id)
        if score == 'up':
            if vu.score == 0:
                vu.score += 5
            else:
                vu.score += 1
        elif score == 'down':
            if vu.score == 0:
                vu.score += 1
            else:
                vu.score -= 1

        # Update score only when it's in rational range, 1 is identified as "New Word", 5 is identified as "Learned"
        if 1 <= vu.score < 6:
            # Set understanding as master when score is greater than 5
            if vu.score >= 5 and not vu.mastered_at:
                vu.mastered_at = timezone.now()
            vu.save()
            self.update_flashcard_progress()

    def update_flashcard_progress(self):
        flashcard = FlashCard.objects.prefetch_related('vocabularies').filter(vocabulary_program=self.program, member=self.member)[0]
        flashcard_vocabs = flashcard.vocabularies.values_list('id', flat=True)
        learned = Count('understandings', filter=(
                (Q(understandings__score__gt=4)) & Q(understandings__vocabulary__in=flashcard_vocabs)))
        member = Member.objects.prefetch_related('understandings').filter(pk=self.member.pk).annotate(learned=learned)
        learned = member[0].learned
        flashcard.progress = (learned / len(flashcard_vocabs)) * 100
        flashcard.save()

    def overall_progress(self):
        # VocabularyUnderstanding.objects.filter(member=self.member, vocabulary__vocabulary_list__program=self.program)
        learned = Count('understandings', filter=(
                (Q(understandings__score__gt=4)) & Q(understandings__vocabulary__vocab_program=self.program)))

        reviewing = Count('understandings', filter=(
                    (Q(understandings__score__gt=0) & Q(understandings__score__lt=5)) & Q(
                understandings__vocabulary__vocab_program=self.program)))
        mem = Member.objects.filter(pk=self.member.pk).annotate(reviewing=reviewing).annotate(learned=learned)
        learned = mem[0].learned
        reviewing = mem[0].reviewing
        total = self.program.vocabularies.count()

        percentage = (learned / total) * 100

        progress = {'learned': learned, 'reviewing': reviewing, 'total': total, 'percentage': percentage}
        return progress
