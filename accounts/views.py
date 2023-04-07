from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin, View
from django.views import generic
from .models import CustomUserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.


class HomePage(generic.TemplateView):
    template_name = "home.html"


class Signup(TemplateResponseMixin, View):
    template_name = "registration/signup.html"
    user = None

    def get_formset(self, data=None):
        return CustomUserCreationForm(data=data)


    def get(self, request, format=None):
        form = self.get_formset()
        return self.render_to_response({
            "form": form
        })

    def post(self, request, format=None):
        form = self.get_formset(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

        return self.render_to_response({
            "form": form
        })