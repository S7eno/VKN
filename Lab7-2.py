import random

nat = "листя  дерево трава ліс камінь"
flo = "фіалка троянда орхідея тюльпан пролісок"

sl1 = nat.split( ) 
sl2 = flo.split( ) 
x =(sl2[4])

slovo_list = list(x)
ss = random.sample(slovo_list,  len(slovo_list))


print(' '.join([str (i) for i in ss]))


