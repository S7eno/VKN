s = input("Введіть символи: ")
n = [i for i in s if i.isupper()]
m = [a for a in s if a.islower()]
s1 = len(n)

s2 = len(m)

print("Великі символи: " + ' '.join([str (i) for i in n]))
print("Всього великих букв: " + str(s1))
print("Малі символи: " + ' '.join([str (i) for i in m]))
print("Всього малих букв: " + str(s2))