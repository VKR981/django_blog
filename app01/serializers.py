from rest_framework.serializers import SlugRelatedField, ModelSerializer, Serializer, HyperlinkedModelSerializer, HyperlinkedIdentityField
from rest_framework.fields import CharField
from django.contrib.auth.models import User
from .models import Comment, Post, Rating


class UserSerializer(Serializer):
    username = CharField(max_length=32)


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'url': {
                "lookup_field": 'slug',
                "view_name": 'api-Post-detail'
            }
        }

    # def create(self,  validated_data):
    #     Post = Post.objects.create(**validated_data)
    #     return Post


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self,  validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment
