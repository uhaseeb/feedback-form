from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import Profile


class CreateProfileView(CreateView):

    template_name = 'create_profile.html'
    model = Profile
    fields = '__all__'
    success_url = 'profiles'


class ProfileListView(ListView):
    template_name = 'listprofile.html'
    model = Profile
    context_object_name = 'profiles'


