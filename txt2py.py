#!/usr/bin/env python
# codig:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

import django
if django.VERSION >= (1, 7):
    django.setup()


def main():
    from threeD.models import threeD
    f = open('web.txt')
    for line in f:
        if(len(line) == 24):
            a, b, c = line.split(',')
            threeD.objects.create(create_data=a, order=b, three_d=c)
    f.close()


if __name__ == '__main__':
    main()
    print('Done!')
