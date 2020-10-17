from django.dispatch import receiver
from django.db.models.signals import post_save

from program.models import ProgramEnrollment


# @receiver(post_save, sender=ProgramEnrollment)
# def create_program_progress(sender, instance, **kwargs):
#     """
#     create_node_relations is triggered after a Node is saved to create additional relations.
#     @param sender: Object that sent this signal
#     @param instance: Instance which is saved
#     @param kwargs: Parameters of saved instance
#     """
#     if kwargs.get('created', False):
#         ProgramProgress.objects.get_or_create(enrollment=instance)
