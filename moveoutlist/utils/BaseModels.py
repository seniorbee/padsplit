import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

USER_MODEL = get_user_model()


class BaseModel(models.Model):
    """Base model for providing uuid, updated_at, created_at fields"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated date"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))

    class Meta:
        abstract = True
