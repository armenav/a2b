# coding: utf-8
import django_tables2 as tables
from main.models import Ride
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

class DriverColumn(tables.Column):
    def render(self, record):
        return mark_safe('<img id="driver-img" width="150px" data-id=' + str(
            record.driver.id) + ' data-toggle="modal" data-target="#myModal" src="%s" />' % escape(
            record.driver.featured_image.image.url))


class RideTable(tables.Table):
    leavedate = tables.Column(verbose_name="Ամսաթիվ")
    driver = DriverColumn(verbose_name="Վարորդ")
    price = tables.Column(verbose_name="Արժեքը")
    fromwhere = tables.Column(verbose_name="Որտեղից")
    towhere = tables.Column(verbose_name="Ուր")



    def render_leavedate(self, value, record):
        return "%s - %s" % (record.leavedate.strftime('%d/%m/%Y %H:%M'), record.endtime.strftime("%H:%M"))

    class Meta:
        model = Ride
        attrs = {"class": "table table-hover"}
        exclude = ("id", "endtime",)
        empty_text = "Ներկայումս մենք չունենք Ձեր ուղղությամբ երթուղիներ, այցելեք մեզ ավելի ուշ։"
