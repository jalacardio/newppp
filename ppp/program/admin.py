from django.contrib import admin

import program.signals as signals

from program.models import VocabularyProgram, Vocabulary, VocabularyUnderstanding, ProgramEnrollment, \
    FlashCard, VocabularyTranslation


class FlashCardAdmin(admin.ModelAdmin):
    raw_id_fields = ("vocabularies",)


class VocabularyUnderstandingAdmin(admin.ModelAdmin):
    raw_id_fields = ("vocabulary",)

class VocabularyTranslationAdmin(admin.ModelAdmin):
    raw_id_fields = ("vocabulary",)


# Register your models here.
admin.site.register(VocabularyProgram)
admin.site.register(ProgramEnrollment)
admin.site.register(VocabularyTranslation, VocabularyTranslationAdmin)
admin.site.register(VocabularyUnderstanding, VocabularyUnderstandingAdmin)
admin.site.register(Vocabulary)
admin.site.register(FlashCard, FlashCardAdmin)
