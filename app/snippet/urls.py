from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import SnippetViewset, TagViewset


router = DefaultRouter()
router.register("snippets", SnippetViewset, "snippet")
router.register("tag", TagViewset, "tag")


urlpatterns = [
    path("", include(router.urls)),
]
