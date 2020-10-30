from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Comment, Post, Rating
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import PostSerializer, CommentSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, permissions, status
from knox.models import AuthToken
from django_filters.rest_framework import DjangoFilterBackend
import logging

# Create your views here.


def index(request):
    return render(request, 'index.html')


class PostAPI(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):

        serializer.save(username=self.request.user)

    def destroy(self, request, *args, **kwargs):
        print('destroy')
        instance = self.get_object()
        response = self.serializer_class(instance).data
        if str(instance.username) == str(request.user.username):
            self.perform_destroy(instance)
            return Response(response)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if str(instance.username) == str(request.user.username):
            # self.perform_destroy(instance)
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class CommentAPI(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Post']

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = self.serializer_class(instance).data
        if str(instance.username) == str(request.user.username):
            self.perform_destroy(instance)
            return Response(response)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if str(instance.username) == str(request.user.username):
            # self.perform_destroy(instance)

            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            comments = Comment.objects.filter(Post=instance.slug)

            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
