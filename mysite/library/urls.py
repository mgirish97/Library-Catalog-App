from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>/", views.item, name="item"),
    path("login/", views.login, name='login')
]