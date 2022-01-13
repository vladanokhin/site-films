from django.urls import path
from . import views
from .views import MoviesView


urlpatterns = [
    path('', MoviesView.as_view())
]