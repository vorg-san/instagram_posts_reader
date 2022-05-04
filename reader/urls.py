from django.urls import path

from . import views

app_name = "reader"
urlpatterns = [
    # ex: /reader/
    path("", views.index, name="index"),
    # ex: /reader/5/
    path("run_bot/", views.run_bot, name="run bot"),
    # path("<int:question_id>/", views.detail, name="detail"),
]
