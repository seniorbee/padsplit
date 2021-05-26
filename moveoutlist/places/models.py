from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.BaseModels import BaseModel

USER_MODEL = get_user_model()


class Address(BaseModel):
    """A model for storing the address data, address is any place that has rooms for rent"""
    owner = models.ForeignKey(USER_MODEL, verbose_name=_('Owner'), on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), max_length=500, null=True, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Room(BaseModel):
    """A single room of a house(address)"""
    address = models.ForeignKey('Address', verbose_name=_('address'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=50, blank=True)

    def __str__(self):
        return self.title


class MoveOut(BaseModel):
    """Table for holding data of move-outs"""
    move_out_date = models.DateField(verbose_name='Move-out date')
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=False)
    last_occupant = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'Move out {self.id}'
