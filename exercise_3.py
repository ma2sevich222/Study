# -*- coding: utf-8 -*-
"""ex_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RN6ELQJl10WpWGMkSh10Lz0p-E1suSNB
"""

def ConquestCampaign(N:int,M:int,L:int,batalion:[int])->int:

  enemy_terra=[[0]*M for _ in range(N) ]
  batalion=[i-1 for i in batalion]

  i=0
  bat_mat=[]
  while i<len(batalion):
    bat_mat.append(batalion[i:i+L])
    i+=L
  
  for indexN, item in enumerate(enemy_terra):
    for indexM,el in enumerate(item):
      lop=[indexN,indexM]
      if lop in bat_mat:
        
        enemy_terra[indexN][indexM]=1

  q = []
  for i in range(N):
    for j in range(M):
      if (enemy_terra[i][j] == 1):
        q.append([i,j])
   

  step = 0

  while (len(q)):
    qsize = len(q)
    while(qsize):
      p = q[0]
      q.remove(q[0])
      i = p[0]
      j = p[1]

      if((j > 0) and enemy_terra[i][j - 1] == 0):
        enemy_terra[i][j - 1] = 1
        q.append([i, j - 1])
                 
      if((i < N-1) and enemy_terra[i + 1][j] == 0):
        enemy_terra[i + 1][j] = 1
        q.append([i + 1, j])
                 
      if((j < N-1) and enemy_terra[i][j + 1] == 0):
        enemy_terra[i][j + 1] = 1
        q.append([i, j + 1])
                 
      if((i > 0) and enemy_terra[i - 1][j] == 0):
        enemy_terra[i - 1][j] = 1
        q.append([i - 1, j])
                 
      if((i > 0) and (j > 0) and enemy_terra[i - 1][j - 1] == 0):
        enemy_terra[i - 1][j - 1] = 1
        q.append([i - 1, j - 1])
                 
      if((i > 0) and (j < (M-1)) and enemy_terra[i - 1][j + 1] == 0):
        enemy_terra[i - 1][j + 1] = 1
        q.append([i - 1, j + 1])
                 
      if((i < (N - 1)) and (j < (M - 1)) and enemy_terra[i + 1][j + 1] == 0):
        enemy_terra[i + 1][j + 1] = 1
        q.append([i + 1, j + 1])
                 
      if((i < (N - 1)) and (j > 0) and enemy_terra[i + 1][j - 1] == 0):
        enemy_terra[i + 1][j - 1] = 1
        q.append([i + 1,j - 1])

      qsize -= 1
             
        
    step += 1
  return(step)