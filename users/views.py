from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'users/users.html'

    # Set user Group on registration
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # One user Group
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)

            # Multiple user Groups
            # for form_ug in form.cleaned_data['groups']:
            #     user_group = Group.objects.get(name=form_ug.name)
            #     user.groups.add(user_group)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})

# Create your views here.

