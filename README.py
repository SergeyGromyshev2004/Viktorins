# Viktorina
import random
a=['8', '2']
b=['8', '2']
h=0
print("Введите ответ")
while len(a)>0:
    s=random.randint(0,len(a)-1)
    print(a[s])
    if input()==b[s]:
        a.pop(s)
        b.pop(s)
    else:
        h+=1
print(f'количество ошибок: {h}')
