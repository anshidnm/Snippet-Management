from django.db import models


class BaseModel(models.Model):
    """
    Abstract model for all other models
    used to provide timestamp of creation
    and updattion by default
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
