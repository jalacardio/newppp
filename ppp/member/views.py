from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse

from member.forms import MemberSignUpForm
from member.models import Member


class MemberSignUpView(CreateView):
    model = Member
    form_class = MemberSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('program:index'))
