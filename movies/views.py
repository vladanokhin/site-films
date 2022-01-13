from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Movie


class MoviesView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies.html', {'movies': movies})

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')    