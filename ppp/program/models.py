from django.db import models
from member.models import Member
from dictionary.models import Word
from django.contrib import admin

#
# class VocabularyBank(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     alias = models.CharField(max_length=255, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return "{}".format(self.name)


class VocabularyProgram(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ProgramEnrollment(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, null=True, blank=True, related_name='enrollments')
    vocabulary_program = models.ForeignKey(
        VocabularyProgram, on_delete=models.CASCADE, null=True, blank=True, related_name='enrollments')
    enrolled_at = models.DateTimeField(blank=True, null=True)


class Vocabulary(models.Model):
    rep = models.CharField(max_length=200)
    vocab_program = models.ForeignKey(VocabularyProgram, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='vocabularies')

    def __str__(self):
        return "{} - {}".format(self.vocab_program.name, self.rep)


class VocabularyTranslation(models.Model):
    rep = models.CharField(max_length=1500)
    speech = models.CharField(max_length=50, null=True, blank=True)
    vocabulary = models.OneToOneField(Vocabulary, on_delete=models.CASCADE, related_name='translation')


class VocabularyUnderstanding(models.Model):
    score = models.IntegerField(default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='understandings')
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, related_name='understandings')
    mastered_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Member:{} - Program:{} - {} : {} - {}".format(self.member.pk, self.vocabulary.vocab_program.pk, self.vocabulary.rep, self.score, self.mastered_at)


class FlashCard(models.Model):
    vocabulary_program = models.ForeignKey(
        VocabularyProgram, on_delete=models.CASCADE, null=True, blank=True, related_name='flashcards')
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, null=True, blank=True, related_name='flashcards')
    vocabularies = models.ManyToManyField(Vocabulary, related_name='flashcards')
    progress = models.DecimalField(default=0.000, max_digits=4, decimal_places=1)
