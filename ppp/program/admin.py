from django.contrib import admin

import program.signals as signals

from program.models import VocabularyBank, VocabularyProgram, Vocabulary, VocabularyUnderstanding, ProgramEnrollment, \
    FlashCard


class VocabularyAdmin(admin.ModelAdmin):
    raw_id_fields = ("word",)


class FlashCardAdmin(admin.ModelAdmin):
    raw_id_fields = ("vocabularies",)


class VocabularyUnderstandingAdmin(admin.ModelAdmin):
    raw_id_fields = ("vocabulary",)


# Register your models here.
admin.site.register(VocabularyProgram)
admin.site.register(ProgramEnrollment)
admin.site.register(VocabularyBank)
admin.site.register(VocabularyUnderstanding, VocabularyUnderstandingAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(FlashCard, FlashCardAdmin)
