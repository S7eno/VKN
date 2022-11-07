import array
import numpy as np 
import random 
masiv_M=np.zeros(( 3,4 ),dtype= int)
for i in range(3): 
    for j in range (4): 
         masiv_M[i][j]=random.randint(0,9) 
         


j = masiv_M[ (masiv_M  < 1  )] = 9


z = np.split(masiv_M , 3,)


print(masiv_M)

print()
print(z)





