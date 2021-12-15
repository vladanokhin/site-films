from django.contrib import admin
from .models import *


admin.site.register([
    Category,
    Actor,
    Genre,
    Movie,
    MovieShots,
    RatingStar,
    Rating,
    Reviews
])