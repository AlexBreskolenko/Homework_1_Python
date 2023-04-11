"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
 вы расплачивались за проезд и получали билет с номером. 
 Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
"""

ticketNumber = 123456

firstPart = ticketNumber // 1000
secondPart = ticketNumber % 1000

sumFirstPart = 0
while firstPart > 0:

    sumFirstPart += firstPart % 10
    firstPart //= 10

sumSecondPart = 0
while secondPart > 0:

    sumSecondPart += secondPart % 10
    secondPart //= 10

if sumFirstPart == sumSecondPart:
    print("{} -> yes".format(ticketNumber))
else:
    print("{} -> no".format(ticketNumber));    