# -*- coding: utf-8 -*-
"""task6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fcoms28ggU9n1lUtCvHrt7s77OtEXh5q
"""

def PatternUnlock(N,hits):
  decode={6:[0,0],1:[0,1],9:[0,2],5:[1,0],2:[1,1],8:[1,2],4:[2,0],3:[2,1],7:[2,2]}
  distance=0
  
  points=[]

  for key in hits:
    points.append(decode[key])

  if len(points)<3:
    distance=(((points[1][0]-points[0][0])**2)+((points[1][1]-points[0][1])**2))**(1/2)
    distance=round(distance,5)
  
  else:


    for i, item  in enumerate(points):
      if i!=0:
        dist=((points[i][0]-points[i-1][0])**2+(points[i][1]-points[i-1][1])**2)**(1/2)
        
        
        distance+=dist

  
  
  replace=".0"
  str_distance=str(round(distance,5))
  for char in replace:
    str_distance = str_distance.replace(char, "")
  

    
  

  return str_distance