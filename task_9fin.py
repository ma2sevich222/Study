# -*- coding: utf-8 -*-
"""Task_9fin.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mr83X7KcBvFt_tF_tksi8sURoDes4Gl1
"""

def TheRabbitsFoot(s,encode):


  remove_space=s.replace(" ", "") 
  M=str(len(remove_space)**(1/2))
  X=int(M[0])
  Y=int(M[2])

  if encode==True:


    
    

    while (X*Y)<len(remove_space):
      X+=1

    coded_string_mat=[]

    coded_string=[remove_space[i:i+Y]for i in range(0,len(remove_space),Y)]

    for word in coded_string:

      let=len(word)

      if let<Y:
        word=word+("@"*(Y-let))
        coded_string_mat.append(word)
      else:
        coded_string_mat.append(word)


    Trans_coded=[list(i) for i in zip(*coded_string_mat)]

    

    coded_sentence=""

    for i in Trans_coded:
      coded_sentence+="".join(i)+' '

    final_sentence=coded_sentence.replace("@","").rstrip()


  else:


    Strings_4_decode=[s[i:i+Y]for i in range(0,len(s),Y)]


    string_4_decode_mat=[]


    for word in Strings_4_decode:

      let=len(word.replace(" ",""))

      if let<Y:
        word=word.replace(" ","")+("@"*(Y-let))
        string_4_decode_mat.append(word)
      else:
        string_4_decode_mat.append(word)

    Trans_decod_mat=[list(i) for i in zip(*string_4_decode_mat)]


    decoded_senntence=""

    for i in Trans_decod_mat:
      decoded_senntence+="".join(i)

    final_sentence=decoded_senntence.replace('@',"")

  return final_sentence