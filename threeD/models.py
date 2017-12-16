# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class threeDList(models.Model):
    '''list of the 3d'''
    three_d = models.CharField(primary_key=True, max_length=3,)
    lost_count = models.IntegerField()
    mix_repeat = models.IntegerField()
    three_d_list = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.three_d


class threeD(models.Model):
    '''discreapt for 3d'''
    td = models.ForeignKey(threeDList)
    data = models.DateField(blank=True, null=True,)
    order = models.CharField(max_length=7,)

    def __unicode__(self):
        return self.td.three_d
