from django.urls import path

from . import views

app_name = "program"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:program_id>/enroll/', views.enroll, name='enroll'),
    path('<int:program_id>/dashboard/', views.dashboard, name='dashboard'),
    path('<int:program_id>/flashcard/', views.flashcard, name='flashcard'),
    path('<int:program_id>/up_score/<int:vocab_id>', views.up_score, name='up_score'),
    path('<int:program_id>/down_score/<int:vocab_id>', views.down_score, name='down_score'),
]
