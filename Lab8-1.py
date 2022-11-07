from array import *
import numpy as np
import random 
A = 8
masiv_A = array('i',[])
for i in range (A):
    x = random.randint(3,15)
    masiv_A.append(x)
print(masiv_A)

masiv_B= array ('i',[0,0,0])
k = 0

k1 = 0
for elemens in masiv_A:
    if elemens %2==1:

        k = k + 1
    else:
        k1 = k1 + 1

masiv_B[0] = k 
masiv_B[1] = k1
masiv_B[2] = sum (masiv_A)
print(masiv_B)

#from array import *
#import numpy as np
#import random 
#A = 8
#masiv_A = array('i',[])
#for i in range (A):
   # x = random.randint(3,15)
    #masiv_A.append(x)
#print(masiv_A)

#masiv_B= array ('i',[0])
#masiv_B = [x for x in masiv_A if not x%2]
#print(masiv_B)

#masiv_B = [v for v in masiv_A if v % 2 != 0]   
#print(masiv_B )

#masiv_B = np.sum(masiv_A) 
#print([masiv_B])