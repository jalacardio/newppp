from django.contrib import admin
from .models import Word, Translation, Meaning, Speech, Phonetic, WordAnalysis

# Register your models here.
admin.site.register(Word)
admin.site.register(Translation)
admin.site.register(Meaning)
admin.site.register(Speech)
admin.site.register(Phonetic)
admin.site.register(WordAnalysis)
