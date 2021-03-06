from logging import getLogger
from datetime import date, timedelta
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput
from rest_framework import generics
from .models import Room, Booking, Guest
from .serializers import GuestSerializer, RoomSerializer, BookingSerializer

log = getLogger(__name__)


class DateInput(TextInput):
    input_type = 'date'


class GuestList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class RoomList(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        if not self.kwargs.get('free', False):
            return Room.objects.all()

        def date_from_string(string):
            return date(*map(int, string.split('/')))

        start_date = self.kwargs.get('date', None)
        end_date = self.kwargs.get('end_date', None)

        if not date:
            start_date = date.today()
        else:
            start_date = date_from_string(start_date)

        if not end_date:
            end_date = start_date
        else:
            end_date = date_from_string(end_date)

        return Room.get_free(start_date, end_date=end_date)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer


    def get_queryset(self):
        year = self.kwargs.get('year', None)
        if year is not None:
            year = int(year)
            month= self.kwargs.get('month', None)
            if month is not None:
                month = int(month)
                day = self.kwargs.get('day', None)
                if day is not None:
                    day = int(day)
                    start = end = date(year, month, day)
                else:
                    start = date(year, month, 1)
                    end = date(year, month + 1, 1) - timedelta(1, 0, 0)
            else:
                start = date(year=year, month=1, day=1)
                end = date(year, 12, 31)
            return Booking.objects.filter(start_date__lte=end,
                                          end_date__gte=start)
        else:
            return Booking.objects.all()


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def test_view(request, *args, **kwargs):
    Formset = inlineformset_factory(
        Room, Booking, exclude=(), extra=5, widgets={
            'guest': TextInput(),
            'start_date': DateInput(),
            'end_date': DateInput(),
            'paid_until': DateInput(),
        })
    room_formsets = {}
    for room in Room.objects.all():
        formset_kwargs = dict(prefix=room.name, instance=room)
        if request.method == 'POST':
            forms = Formset(request.POST, **formset_kwargs)
            if forms.is_valid():
                forms.save()
                forms = Formset(**formset_kwargs)
        else:
            forms = Formset(**formset_kwargs)
        room_formsets.update({room: forms})
    return render(request, "book/room_form.html", {
        "room_formsets": room_formsets,
    })

