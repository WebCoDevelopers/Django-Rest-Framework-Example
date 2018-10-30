from django.shortcuts import render
from django.http import HttpResponse;
from .models import (Language,Paradigm,Programmer);
from rest_framework import viewsets,permissions;
from .serializer import (LanguageSerializer,ParadigmSerializer,ProgrammerSerializer);
def home(request):
    output ="""
    <h1>Welcome To Home Page</h1><br>
    <h2>Simple Example Of Use Django Rest Framewok </h2>
    <hr><hr>
    <h1> Go To Apis <a href='apis/'>APIS</a></h1>
    """;
    return HttpResponse(output);
class LanguageView(viewsets.ModelViewSet):
    queryset=Language.objects.all();
    serializer_class=LanguageSerializer;
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly];
class ParadigmView(viewsets.ModelViewSet):
    queryset=Paradigm.objects.all();
    serializer_class=ParadigmSerializer;
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly];
class ProgrammerView(viewsets.ModelViewSet):
    queryset=Programmer.objects.all();
    serializer_class=ProgrammerSerializer;
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly];
