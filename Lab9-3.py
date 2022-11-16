num1 = {1 :"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",9:"Nine "  } 
while True:
    num = input("Введіть цифру  (або Enter для виходу ): ")
    if not num :
        break
    sl = input("Введіть слово: ")
   
    
    dov = num1.get(num , None)
    if dov is None:
        num1[num ] = sl   

for key , value in num1.items():
    print (key, "-", value)    