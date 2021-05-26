from django.contrib import admin

from places.models import Address, Room, MoveOut


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(MoveOut)
class MoveOutAdmin(admin.ModelAdmin):
    pass
