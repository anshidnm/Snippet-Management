from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import SnippetSerializer, TagSerializer, TagDetailsSerializer
from .models import Snippet, Tag


class SnippetViewset(ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.select_related("tag", "created_by").order_by("-id")
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["title", "tag__title"]


class TagViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = TagDetailsSerializer
    queryset = Tag.objects.prefetch_related("snippets").order_by("-id")
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["title"]
