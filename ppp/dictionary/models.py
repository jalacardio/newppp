from django.db import models


class Word(models.Model):
    rep = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.rep)


class Translation(models.Model):
    rep = models.CharField(max_length=1500)
    category = models.CharField(max_length=50, null=True, blank=True)
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='translations')

    def __str__(self):
        return "{} - {}".format(self.word.rep, ", ".join([i['rep'] for i in list(self.speeches.values('rep'))]))


class Meaning(models.Model):
    rep = models.CharField(max_length=1500)
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='meanings')
    source = models.CharField(max_length=100)

    def __str__(self):
        return "{}- {}".format(self.word.rep)


class Speech(models.Model):
    rep = models.CharField(max_length=50)
    meanings = models.ManyToManyField(Meaning, related_name='speeches')
    translations = models.ManyToManyField(Translation, related_name='speeches')

    def __str__(self):
        return "{}".format(self.rep)


class Phonetic(models.Model):
    kk = models.CharField(max_length=255)
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='phonetic')


class WordAnalysis(models.Model):
    total_occurrence = models.IntegerField(default=0)
    word = models.OneToOneField(Word,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                related_name='analysis')

    def __str__(self):
        return "{} - {}".format(self.word.rep, self.total_occurrence)

# class Tense(models.Model):
#     parent = models.ForeignKey(
#         Word, on_delete=models.CASCADE, related_name='parent')
#     child = models.ForeignKey(
#         Word, on_delete=models.CASCADE, related_name='child')
#     rep = models.CharField(max_length=255)
#
#     def __str__(self):
#         return "{}".format(self.rep)
