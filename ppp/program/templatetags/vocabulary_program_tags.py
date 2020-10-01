from program.services.vocabulary_program_service import VocabularyProgramService
from django import template

register = template.Library()


@register.filter(name='is_enrolled')
def is_enrolled(member_id, program_id):
    service = VocabularyProgramService(program_id, member_id)
    is_member_enrolled = service.is_enrolled()
    return is_member_enrolled

