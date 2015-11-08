from django.core.urlresolvers import reverse
from django.db import models
from datetime import date

class Room(models.Model):
    name = models.SlugField(max_length=256, help_text="Name", primary_key=True)
    beds = models.SmallIntegerField(help_text="Number of beds.")
    shared = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    price_per_day = models.DecimalField(decimal_places=2, max_digits=5)
    price_per_week = models.DecimalField(decimal_places=2, max_digits=5)

    @property
    def free(self):
        taken = self.bookings.count()
        return self.beds - taken

    def get_absolute_url(self):
        return reverse('book.room', kwargs={'slug': self.slug})

    def __str__(self):
        return "{name} ({free} of {beds} free)".format(
            name=self.name, free=self.free, beds=self.beds)

    class Meta:
        ordering = ('name', )
        default_related_name = 'rooms'


class Guest(models.Model):
    name = models.SlugField(max_length=256, unique=True, primary_key=True)
    note = models.TextField(max_length=2048, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'guests'

class Booking(models.Model):
    guest = models.ForeignKey(Guest, related_name='bookings')
    room = models.ForeignKey(Room)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    paid_until = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    @property
    def paid(self):
        if self.paid_until is not None and self.end_date is not None:
            return self.paid_until >= self.end_date
        elif self.end_date is None:
            return self.paid_until >= date.today()
        else:
            return False

    def __str__(self):
        return "{guest} in {room} (from {start} to {end}); paid: {paid}".format(
            guest=self.guest, room=self.room.name, start=self.start_date,
            end=self.end_date, paid=self.paid)

    class Meta:
        ordering = ('start_date', 'end_date')
        default_related_name = 'bookings'
