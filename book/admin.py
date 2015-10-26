from django.contrib import admin
from .models import Room, Guest, Booking

admin.site.register(Guest)
admin.site.register(Booking)


class BookingInline(admin.TabularInline):
    model = Booking

    def get_max_num(self, request, obj=None, **kwargs):
        if obj is not None:
            return obj.beds
        return 0

    def get_extra(self, request, obj=None, **kwargs):
        return obj.free if obj is not None else 0


class RoomAdmin(admin.ModelAdmin):
    inlines = [
        BookingInline,
    ]


admin.site.register(Room, RoomAdmin)
