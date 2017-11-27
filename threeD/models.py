# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class threeD(models.Model):
    '''discreapt for 3d'''
    create_data = models.DateField(blank=True, null=True,)
    order = models.CharField(max_length=7,)
    three_d = models.CharField(max_length=3,)

    def __unicode__(self):
        return self.three_d
