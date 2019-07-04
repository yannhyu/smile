import requests
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from core.models import Comment
from core.serializers import CommentSerializer


class TestCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def retrieve(self, request, *args, **kwargs):
        # return Response({'something': 'my custom JSON'})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        # return Response({'something': 'my custom JSON'})
        comment = Comment(email='leila@example.com', content='foo bar')
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class MyOwnView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
