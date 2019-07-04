from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


class LaunchpadSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=30)
