from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from member.models import User, Member


class MemberSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        member = Member.objects.create(user=user)
        # student.interests.add(*self.cleaned_data.get('interests'))
        return user
