from django.urls import path

from social import views



urlpatterns=[
    path("login",views.Loginview.as_view(),name="signin"),
    path("register",views.Registerview.as_view(),name="register")

]