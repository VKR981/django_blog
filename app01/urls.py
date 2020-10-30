from django.conf import settings
from django.urls import path, include
from . import views
from .views import PostAPI, CommentAPI, RatingAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Post', PostAPI)
router.register('comment', CommentAPI)
router.register('rating', RatingAPI)

urlpatterns = [

    path("api/v1/", include(router.urls)),



]
