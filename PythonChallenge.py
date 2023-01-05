import numpy as np
import random

def PythonChallenge():
  flag = 0
  list = np.arange(1,10,step=1)
  
  while flag == 0:
     A = random.choice(list)
     B = random.choice(list)
     C = A*B

     if C == 4:
        print('Success! Your values for A and B are: A =', A,'and B =',B)
        flag = 1
     else: 
      print( 'A =',A,'and C =',C)

PythonChallenge() 
