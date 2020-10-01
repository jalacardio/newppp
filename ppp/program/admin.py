from django.contrib import admin
from program.models import VocabularyProgram, VocabularyList, Vocabulary, FlashCard, VocabularyUnderstanding

# Register your models here.
admin.site.register(VocabularyProgram)
admin.site.register(VocabularyList)
admin.site.register(VocabularyUnderstanding)
admin.site.register(Vocabulary)
admin.site.register(FlashCard)
