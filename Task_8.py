"""
Задача 8:
 Требуется определить, можно ли от шоколадки размером
 n × m долек отломить k долек, если разрешается сделать один разлом по прямой
  между дольками (то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no
"""

n = 3
m = 2
k = 4

if k < m*n and (k%m==0 or k%n==0):
    print("{} {} {} -> yes".format(n, m, k))
else:
    print("{} {} {} -> no".format(n, m, k))