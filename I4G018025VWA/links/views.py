from django.shortcuts import render
from rest_framework import serializers
from . import serializers
# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)

    serializer_class = LinkSerializer
class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)

    serializer_class = LinkSerializer
class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)

    serializer_class = LinkSerializer
class PostUpdateApi(UpdateAPIView):
    queryset = Link.object.filter(active=True)

    serializer_class = LinkSerializer
class PostDeleteApi(DestroyAPIView):
    queryset= Link.objects.filter(active=True)

    serializer_class = LinkSerializer