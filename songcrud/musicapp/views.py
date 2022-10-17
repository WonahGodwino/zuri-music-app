from tkinter import CENTER
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(" <center><strong>Hello, Welcome to the World of Zuri Music.</strong><b><br/> <h2>Congratulations on successfull creation of first adjango App</h2><strong><h2> Zuri Music App</h2></strong><img src='https://st2.depositphotos.com/2075965/6365/v/600/depositphotos_63653511-stock-illustration-abstract-colorful-music-notes.jpg' alt ='Music background'<br/> <strong> <h4>Enjoy your Music on the Go!</h4></strong><audio controls autoplay><source src='https://trendybeatz.com/download-mp3/27572/rema-calm-down-new-song' type='audio/ogg'>Your browser does not support the audio element.</audio></center>")