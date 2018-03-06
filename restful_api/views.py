from django.shortcuts import render
from rest_framework import viewsets
from .models import Portable_Object
from .serializers import Portable_Object_Serializer
# Create your views here.

class Portable_Object_View(viewsets.ModelViewSet):
	queryset =  Portable_Object.objects.all()
	serializer_class = Portable_Object_Serializer