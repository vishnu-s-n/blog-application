from django.shortcuts import render,redirect

from django.views.generic import View

from social import forms

from django.contrib.auth.models import User

# Create your views here.

class Loginview(View):

    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self,request,*args,**kwargs):
        pass

class Registerview(View):
    def get(self, request, *args, **kwargs):
        form = forms.RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        # print(request.POST.get("firstname"))
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")

        return render(request, "register.html")






