# Clouds
from random import randint
# ЗАДАЧА А1
n = 20
i = 0
a = []*n
a=[randint(50,150) for i in range(n)]
print(a)
print ('max ',max(a),' ind', a.index(max(a)))
print ('min ',min(a),' ind', a.index(min(a)))

#ЗАДАЧА А2

dlin = int(input("введите целое число"))
spisok =[]*dlin
spisok=[randint(50,150) for i in range(dlin)]
spisok[dlin-1] = 0
print(spisok)
print ('max ',max(spisok),' ind', spisok.index(max(spisok)))
print ('min ',min(spisok),' ind', spisok.index(min(spisok)))
