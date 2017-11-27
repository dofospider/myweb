# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from threeD.models import threeD
# Register your models here.


class threeDAdmin(admin.ModelAdmin):
    list_display = ('create_data', 'order', 'three_d')


admin.site.register(threeD, threeDAdmin)
