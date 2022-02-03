from multiprocessing import managers
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
  return Response('Our API')

@api_view(['GET'])
def getNotes(request):
  notes = Note.objects.all()
  serializer = NoteSerializer(notes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getNote(request, noteId):
  note = Note.objects.get(id=noteId)
  serializer = NoteSerializer(note, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
  data = request.data
  note = Note.objects.create(
    body = data['body']
  )
  

@api_view(['PUT'])
def updateNote(request, noteId):
  data = request.data
  note = Note.objects.get(id=noteId)
  serializer = NoteSerializer(instance=note, data=data)
  
  if serializer.is_valid():
    serializer.save()
    
  return response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, noteId):
  note = Note.objects.get(id=noteId)
  note.delete()
  return response("Note deleted succesfully")
  
  
    
