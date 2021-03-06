#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:55:26 2017

@author: dawkiny
"""

from pydemia.manufacture.Lot import wafer, displaypanel

alot = wafer(fac_id='Factory1', lot_cd='ABC', end_tm='20161101123456', size=(50, 30), unit_cnt=20, pattern=['P', 'F'], p=[.7, .3])
blot = displaypanel(fac_id='Factory2', lot_cd='BBC', end_tm='20161101123456', size=(60, 20), unit_cnt=5, pattern=['P', 'B', 'F'], p=[.8, 0.15, .05])

alot.groupby(['unit_id', 'val'])['end_tm'].count()
blot.groupby(['unit_id', 'val'])['end_tm'].count()
len(alot[alot.unit_id=='01'])
len(blot[blot.unit_id=='01'])

aplt = wafer.unitplot(alot, columns=['xcoord', 'ycoord'], lot_id='', unit_id='02', val='val', figsize=(12, 9), pattern=['F'], m=['s'], s=[50], c=['red'], a=[.5], shown='y')
bplt = displaypanel.unitplot(blot, columns=['xcoord', 'ycoord'], lot_id='', unit_id='02', pattern=['B', 'F'], val='val', m=['s', 'o'], s=[50, 50], c=['red', 'blue'], a=[.5, .5], shown='n')

aplt.show()
bplt.show()


len(alot.groupby('unit_id').groups)
len(alot.groupby('unit_id').groups.items())
alot.groupby('unit_id').groups
alot.groupby('unit_id').groups.items()
alot.groupby('unit_id')['val']

