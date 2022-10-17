from tkinter import CENTER
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center>Hello, world. You're at the Music app index.<b><br/> <h2>Congratulations on successfull creation of first adjango App</h2> </center>")