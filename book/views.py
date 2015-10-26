from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput
from .models import Room, Booking

class RoomUpdate(UpdateView):
    fields = ['slug', 'beds', 'shared', 'private', 'price_per_day', 'price_per_week']
    model = Room


class DateInput(TextInput):
    input_type = 'date'


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
        formset_kwargs = dict(prefix=room.slug, instance=room)
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

