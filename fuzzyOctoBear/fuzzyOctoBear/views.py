from django.shortcuts import render
import pdb


def home(request):
	return render( request, "home.html" )


def hello(request):
	return render( request, "home.html" )