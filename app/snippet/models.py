from core.models import BaseModel
from django.contrib.auth.models import User
from django.db import models


class Tag(BaseModel):
    """
    Model to store tag information
    """

    title = models.CharField(max_length=100, unique=True)


class Snippet(BaseModel):
    """
    Model to store snippet information
    """

    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="snippets")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
