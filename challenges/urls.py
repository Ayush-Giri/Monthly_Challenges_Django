from django.urls import path
import challenges.views as views

urlpatterns = [
    path("", views.welcome, name="index"),
    # path("ayush", views.show_ayush_details, name="giri"),
    path("<int:month>", views.monthly_challenge_by_number), # this will check if the dynamic segment can be converted
    # into a int and if it can be converted than it converts it to number and then when that dynamic value is passed
    # into the view function than the value is int
    path("<str:month>", views.monthly_challenge, name="month-challenge"), # here is also the same concept but instead of int here it is integer

]