from django.shortcuts import render
from rest_framework import viewsets
from .models import HereWeGo
from .serializers import HereWeGoSerializer

# Create your views here.
class HereWeGoView(viewsets.ModelViewSet):
    queryset = HereWeGo.objects.all()
    serializer_class = HereWeGoSerializer