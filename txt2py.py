#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

import django
import string
if django.VERSION >= (1, 7):
    django.setup()

# """


def main():
    from threeD.models import threeD
    from threeD.models import threeDList
    f = open('end.txt')
    for line in f:
        if(len(line) > 20):
            # gengxin threeD data
            a, b, c = line.split(',')
            c = c[0:3]
            k = threeDList.objects.get(three_d=c)
            threeD.objects.create(data=a, order=b, td=k,)

            # gengxin threeDList data

            if (k.mix_repeat > k.lost_count) or (k.mix_repeat == -1):
                k.mix_repeat = k.lost_count
            k.lost_count = 0
            k.three_d_list = k.three_d_list + a + ','
            k.save()

            m = threeDList.objects.exclude(three_d=c)
            # print(m)
            for i in m:
                print(i.lost_count)
                i.lost_count = i.lost_count + 1
                i.save()

    f.close()


"""


def main():
    '''3dlist init'''
    from threeD.models import threeDList

    for i in range(0, 1000):
        if i < 100:
            if i < 10:
                k = '00' + str(i)
            else:
                k = '0' + str(i)
        else:
            k = str(i)

        threeDList.objects.create(
            three_d=k, lost_count=0, mix_repeat=-1, three_d_list='')
"""

if __name__ == '__main__':
    main()
    print('Done!')
