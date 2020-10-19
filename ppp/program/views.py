from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models.functions import Length

from program.models import VocabularyProgram
from program.services.vocabulary_program_service import VocabularyProgramService
from member.models import Member


def index(request):
    programs = VocabularyProgram.objects.all()

    context = {
        'programs': programs
    }
    return render(request, 'program/index.html', context)


def enroll(request, program_id):
    current_user = request.user
    service = VocabularyProgramService(program_id, current_user.id)
    service.enroll()
    flashcard = service.get_flash_card()
    context = {
        'flashcard': flashcard
    }
    return render(request, 'program/flashcard.html', context)


def dashboard(request, program_id):
    current_user = request.user
    service = VocabularyProgramService(program_id, current_user.id)
    service.enroll()
    flashcard = service.get_flash_card()
    current_progress = service.overall_progress()
    context = {
        'program': service.program,
        'flashcard': flashcard,
        'current_progress': current_progress
    }
    return render(request, 'program/vocabulary_program/dashboard.html', context)


def new_flashcard(request, program_id):
    current_user = request.user
    service = VocabularyProgramService(program_id, current_user.id)
    flashcard = service.init_flash_card()
    context = {
        'flashcard': flashcard
    }
    return render(request, 'program/flashcard.html', context)


def flashcard(request, program_id):
    current_user = request.user
    service = VocabularyProgramService(program_id, current_user.id)
    flash_card = service.get_flash_card()
    vocab, understanding = service.get_vocabulary_from_flashcard(flash_card.id)
    context = {
        'flashcard': flash_card,
        'vocabulary': vocab,
        'understanding': understanding,
        'vocab_translation': vocab.word.translations,
        'program': service.program
    }
    return render(request, 'program/flashcard.html', context)


def up_score(request, program_id, vocab_id):
    current_user = request.user
    service = VocabularyProgramService(program_id, current_user.id)
    service.update_vocabulary_understanding(vocab_id, 'up')

    return redirect('program:flashcard', program_id=program_id)


def down_score(request, program_id, vocab_id):
    current_user = request.user
    service = VocabularyProgramService(program_id, current_user.id)
    service.update_vocabulary_understanding(vocab_id, 'down')

    return redirect('program:flashcard', program_id=program_id)
