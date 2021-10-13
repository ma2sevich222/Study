#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:57:12 2021

@author: ma2sevich
"""
def odometer(N:[int])-> int:
  return ((N[-2]+N[0])/2)*N[-1]

