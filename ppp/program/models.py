from django.db import models
from member.models import Member


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
        VocabularyProgram, on_delete=models.CASCADE, null=True, blank=True, related_name='vocabulary_programs')
    enrolled_at = models.DateTimeField(blank=True, null=True)


class FlashCard(models.Model):
    vocabulary_program = models.ForeignKey(
        VocabularyProgram, on_delete=models.CASCADE, related_name='sub_programs')
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='sub_programs')
    created_at = models.DateTimeField(blank=True, null=True)


class VocabularyList(models.Model):
    program = models.OneToOneField(
        VocabularyProgram, on_delete=models.CASCADE, null=True, blank=True, related_name='vocabulary_list')


class Vocabulary(models.Model):
    rep = models.CharField(max_length=255)
    translation = models.CharField(max_length=255, null=True, blank=True)
    vocabulary_list = models.ForeignKey(VocabularyList, on_delete=models.CASCADE, related_name='vocabularies')
    flash_card = models.ManyToManyField(FlashCard, blank=True,  related_name='vocabularies')

    def __str__(self):
        return "{}".format(self.rep)


class VocabularyUnderstanding(models.Model):
    score = models.IntegerField(default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='vocabulary_understandings')
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, related_name='understandings')

    def __str__(self):
        return "{} - {} : {}".format(self.member.pk, self.vocabulary.rep, self.score)
