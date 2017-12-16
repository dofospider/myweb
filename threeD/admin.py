# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from threeD.models import threeD
from threeD.models import threeDList
# Register your models here.


class threeDAdmin(admin.ModelAdmin):
    list_display = ('data', 'order', 'td')


admin.site.register(threeD, threeDAdmin)


class threeDListAdmin(admin.ModelAdmin):
    list_display = ('three_d', 'lost_count', 'mix_repeat', 'three_d_list')
    ordering = ('three_d',)


# admin.site.register(threeDList, )
admin.site.register(threeDList, threeDListAdmin)


# admin.site.register(threeDList)
# # admin.site.register(threeD)
