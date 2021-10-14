#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:57:12 2021

@author: ma2sevich
"""
def odometer(N:[int])-> int:
  speed = N[::2]
  time = b[1::2]
  time.insert(0,0)
  dif_time=[time[i+1]-time[i] for i in range(len(time)-1)]
  return sum([x * y for x, y in zip(speed,dif_time)])
