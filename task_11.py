# -*- coding: utf-8 -*-
"""Task_11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FWQypAua4mp_PV4seO5lB8kGrv2c1MLq
"""

def BigMinus(s1,s2):

  len_s1,len_s2=len(s1),len(s2)

  diif=''

  if len_s1==len_s2:

    s1=s1[::-1]
    
    s2=s2[::-1]

    sum_s1=sum(int(x) for x in s1)
    sum_s2=sum(int(y) for y in s2)

    if sum_s1>=sum_s2:
     
      for a,b in zip(s1,s2):
        if int(a)-int(b)>=0:
        
          diif+=str(int(a)-int(b))
        else:
          diif+=str(int(a)-int(b)+10)
        
    else:
      
      for a,b in zip(s1,s2):
        if int(b)-int(a)>=0:
          
          
          diif+=str(int(b)-int(a))
          
        
        else:
          diif+=str(int(b)-int(a)+10)
          







  if len_s1>len_s2:

    s2=((len_s1-len_s2)*'0')+s2
    
  
    s1=s1[::-1]
    
    s2=s2[::-1]
    
    
    for a,b in zip(s1,s2):
      if int(a)-int(b)>=0:
        diif+=str(int(a)-int(b))
      else:
        diif+=str(int(a)-int(b)+10)

  if len_s2>len_s1:
    s1=((len_s2-len_s1)*'0')+s1
    

    s1=s1[::-1]
    
    s2=s2[::-1]
    

    for a,b in zip(s1,s2):
      if int(b)-int(a)>=0:
        diif+=str((int(b)-int(a)))
        
      else:
        diif+=str(int(b)-int(a)+10)

  diif=str(diif[::-1])
  diif=diif.lstrip('0') or '0'

  

  
      





        

  return str(diif)