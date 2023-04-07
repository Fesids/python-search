from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateResponseMixin, View
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Profile
from .forms import UpdateProfileForm
# Create your views here.


class ProfileDetail(TemplateResponseMixin, View):
    template_name = 'profile/manage/detail_profile.html'
    model = Profile
    profile = None


    def dispatch(self, request, *args, **kwargs):
        # id = kwargs.id
        user = request.user
        self.profile = get_object_or_404(Profile, user=user)
        return super().dispatch(request)

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            "profile": self.profile
        })


class UpdateProfilesViews(TemplateResponseMixin, View):
    template_name = "profile/manage/update_profile.html"
    profile = None

    def get_formset(self, data=None):
        return UpdateProfileForm(instance=self.profile, data=data)

    def dispatch(self, request, *args, **kwargs):
        # id =kwargs.id
        user = request.user
        self.profile = get_object_or_404(Profile, user=user)
        return super().dispatch(request)

    def get(self, request, format=None):
        form = self.get_formset()
        return self.render_to_response({
            "form": form,
            "profile": self.profile
        })

    def post(self, request, format=None):

        form = UpdateProfileForm(request.POST, request.FILES, instance=self.profile)
        if form.is_valid():
            form.save()
            return redirect("detail")

        return self.render_to_response({
            "form": form,
            "profile": self.profile
        })



class TesteProfile(TemplateResponseMixin, View):
    template_name = "profile/manage/teste_profile.html"
    model = Profile
    profile = None

    def dispatch(self, request, *args, **kwargs):
        # id = kwargs.id
        user = request.user
        self.profile = get_object_or_404(Profile, user=user)
        return super().dispatch(request)

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            "profile": self.profile
        })


