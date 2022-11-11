from tkinter import CENTER
from django.shortcuts import render
from .models import Artiste ,Song, Lyric
from .serializers import ArtisteSerializer #SongSerializer, LyricsSerializer
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def index(request):
    return HttpResponse(" <center><strong>Hello, Welcome to the World of Zuri Music.</strong><b><br/> <h2>Congratulations on successfull creation of first adjango App</h2><strong><h2> Zuri Music App</h2></strong><img src='https://st2.depositphotos.com/2075965/6365/v/600/depositphotos_63653511-stock-illustration-abstract-colorful-music-notes.jpg' alt ='Music background'<br/> <strong> <h4>Enjoy your Music on the Go!</h4></strong><audio controls autoplay><source src='https://trendybeatz.com/download-mp3/27572/rema-calm-down-new-song' type='audio/ogg'>Your browser does not support the audio element.</audio></center>")


@csrf_exempt
def ArtistesView(request):

    if request.method == 'GET':
        Artistes = Artiste.objects.all() #queryset
        serializer = ArtisteSerializer(Artistes, many = True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        #Artistes = Artiste.objects.all() #queryset
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data = data)
        
        #if Artistes.objects.filter(**request.data).exists():
            #raise serializer.ValidationError('This data already exists')

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def view_artiste(request,pk):
    
    try:
        artiste_detail = Artiste.objects.get(pk=pk)
    
    except artiste_detail.DoesNotExist:
        return HttpResponse(status=404)

    
    if request.method == 'GET':
        serializer = ArtisteSerializer(artiste_detail)
        return JsonResponse(serializer.data)
        
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer =ArtisteSerializer(artiste_detail,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        artiste_detail.delete()
        return HttpResponse(status= 204)


    



    '''elif request.method == 'DELETE':
        if Artistes.Objects.filter(**request.data).exist():
            serializer.delete()
            raise serializer.Validation('The data has been deleted')
        else :
          raise serializer.ValidationError('Record does not exist, check and try again')'''