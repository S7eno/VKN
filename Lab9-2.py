slova =  input("Введіть рядок слів:" ,)
kil = len(slova.split())
s2 = ''
for i in slova.rstrip('.').split():
   if slova.count(i) == 1: s2 += ' ' + i


print( "Kількість слів:"  , kil )
print("Унікальні слова:" , *set(str(slova).split()))
print("Cлова, що зустрічаються один раз:" , s2)