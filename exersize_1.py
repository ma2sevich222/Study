#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:03:42 2021

@author: ma2sevich
"""


def squirrel(N:int)-> int:
  factorial = 1
  for i in range(2, N+1):
    factorial *= i
  return int(str(factorial)[:1])