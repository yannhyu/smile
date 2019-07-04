from collections import namedtuple
import json
import requests
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from core.models import Comment, Launchpad
from core.serializers import CommentSerializer, LaunchpadSerializer

def get_spacexdata_source():
    SPACEX_URL = 'https://api.spacexdata.com/v2/launchpads'
    response = requests.get(SPACEX_URL)
    assert(response.status_code == 200)
    data = response.text
    # Parse JSON into an object with attributes corresponding to dict keys.
    launchpads = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    return launchpads


class LaunchpadViewSet(viewsets.ModelViewSet):
    queryset = Launchpad.objects.all()
    serializer_class = LaunchpadSerializer
    def list(self, request, *args, **kwargs):
        launchpad = Launchpad(
            id='kwajalein_atoll',
            name='Kwajalein Atoll Omelek Island',
            status='retired')
        launchpad2 = Launchpad(
            id='kwajalein_atoll 2',
            name='Kwajalein Atoll Omelek Island 2',
            status='retired')
        launchpads = get_spacexdata_source()
        serializer = LaunchpadSerializer(launchpads, many=True)
        return Response(serializer.data)


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
