from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Books
from .serializers import BooksSerializer

# Create your views here.
class BooksViewSet(ModelViewSet):
  queryset = Books.objects.all()
  serializer_class = BooksSerializer