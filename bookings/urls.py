"""bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import book.views
from datetime import date


today = date.today()
date_regex = r'2\d{3}/[1-9][0-9]?/[0-9]+'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^guest/(?P<pk>[a-zA-Z0-9]*)/?', book.views.GuestDetail.as_view()),
    url(r'^guests/?$', book.views.GuestList.as_view()),
    url(r'^room/(?P<pk>[a-zA-Z0-9]*)/?', book.views.RoomDetail.as_view()),
    url(r'^rooms/?$', book.views.RoomList.as_view()),
    url(r'^booking/(?P<pk>[0-9]*)/?', book.views.BookingDetail.as_view()),
    url(r'^bookings/((?P<year>2\d{3})/((?P<month>(1[0-2]|[0-9]))?/(?P<day>[0-9]+)?)?)?/?$',
        book.views.BookingList.as_view()),
    url(r'^bookings/today/?$', book.views.BookingList.as_view(), kwargs=dict(
         day=today.day, month=today.month, year=today.year
    )),
    url(r'^rooms/(?P<free>free)/((?P<date>{date_regex})(/(?P<end_date>{date_regex}))?)?/?$'.format(date_regex=date_regex), book.views.RoomList.as_view()),
    url(r'^/?$', book.views.test_view)
]
