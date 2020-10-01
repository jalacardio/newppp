from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models.functions import Length

from dictionary.models import Word


def index(request):
    return render(request, 'dictionary/index.html')

def detail(request, word):
    word_object = Word.objects.prefetch_related('translations', 'phonetic', 'translations__speeches').get(rep=word)

    context = {
        'word': word_object,
        # 'tenses': tenses
    }
    return render(request, 'dictionary/detail.html', context)

def search(request):
    word = request.GET['word']
    word = word.lower()
    results = Word.objects.filter(rep__iregex=r"{0}".format("^{}[a-zA-Z]*".format(word))).order_by(Length('rep').asc())[:10]
    # results = Word.objects.filter(rep__iregex=r"{0}".format("^{}[a-zA-Z]+".format(word))).order_by(Length('rep').asc(), 'analysis__total_occurrence')[:10]
    data = []
    for result in results:
        data.append({
            "id": result.id,
            "word": result.rep
        })
    return JsonResponse({"result": data})
