from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import LinkSerializer
from .models import SourceLinks


class LinksView(ListAPIView):
    serializer_class = LinkSerializer
    queryset = SourceLinks.objects.all()