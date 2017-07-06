from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	movies = Movie.objects.order_by('-vrijeme')
	return render(request, 'moviefinder/index.html', {'movies': movies})