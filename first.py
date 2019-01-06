print("Hello world!")
print(3 + 7)
print(6 - 4)
print(3 * 4)
print(25 / 5)
print(-5 * 5)
print(-(-5 * 5))
print(--5) # выведет 5
print(+5)
print(100/3)
print(5 + 5.0)
print(5**2) # степень
print(20//6) # выведет 3
print(20%6) # выведет 2

print('Hi!!')
print("Hi!!")
print("Hi!! \"Alex") # экранирование
print("Hi!! \nAlex")
print('''Hi!! 
Alex''') # многострочное сообщение
input('What is your name?: ')
print(input('What is your name?: '))
test = 10
print(test)
a = input('Введите первое число: ')
b = input('Введите второе число: ')
print(a + b) # если а и b например 2 выведет 22
print(int(a) + int(b))
print('Первая строка' + 'Вторая строка') # конкатенация строк
print("2" + "2") # 22
print("Привет" * 4) # 4 раза выводим Привет
name = input('Введите Ваше имя: ')
count = input('Сколько раз умножить: ')
print( name * int(count))
print(4 * "Привет") # 4 раза выводим Привет

test = 'Test'
test2 = 2
print(test + str(test2)) # int() str() float()
# 34test - ошибка. недьзя начинать с цифры переменную. Питон чувствительный к регистру
test = 10
Test = 20
print(test)
print(Test)
del test # удаляем переменную
# МЕТАСИНТАКСИЧЕСКИЕ ПЕРМЕННЫЕ. Их всего две foo, bar
# In-Place (местные) операторы += -= *= /= %=
test = 10
test = test + 10
test += 10
print(test)
test = 'Alex'
test *= 5
print(test) # 5 раз выведет Alex
x = 5
# x++
print(x) # Ошибка! В питоне так нельзя( Нужно так х += 1

test = True # boolean
test2 = False
print(test)
print(10 == 11)
print(10 != 11)
print(10 > 11)
print(10 >= 10)
# Лексиграфическое сравнение. У каждой буквы есть свой вес. Test > Tesa так как t > a
print("Test" > "Tesa") # регистр не влияет

pogoda = 'Зима'
time = 'Night'
if pogoda == 'Зима':
	print('Сейчас холодная погода') # табуляция обязательна!!!
	print('Ok')
	if time == 'Night':
		print('Еще и ночь')
	if time == 'Morning':
		print('Можно идти')
if pogoda == 'Дождь':
	print('Сейчас дождливая погода')
print('Program ended.')

name = 'Sasha'
if name == 'Lesha':
	print('Hello')
elif name == 'Sasha':
	print('Hi, Sasha!')
else:
	print('Bye!')

if pogoda == 'Дождь' and ( time == 'Ночь' or time == 'Вечер' ):
    print('Hello')

if not pogoda == 'Дождь':
	print('Что-то')
# Приоритетность операторов. Самый высокий приоритет у (), далее **, * /, + -

test = True

while test:
	print('Hi')
	test = False
	
i = 1
while i <= 5:
	print(i)
	if i == 4:
		break # выход из цикла
	i = i + 1

# while 1 == 1: # бесконечный цикл
#	print('Hi')
	
number = 0
while number <= 10:
	number += 1
	if (number % 2) != 0:
		continue
	print('Chetnoe chislo ' + str(number))

test = [1, 2, 3, [4, 5, 6]]
print(test)
print(test[2])	
print(test[3][2])	
	
test = ['a', 'b', 'c', ['d', 'e', 'f']]	
test = [1, 2, 3]
print(test * 2) # дублирует строку 2 раза
print(test + [4, 5, 6]) # добавляем	
test = 'Tester'
print(test[5])	
test = ['Alex Ter', 'Tony Stark', 'Lenny Flawes']
if 'Alex Ter' in test: # можно и с числами
	print('Pravda')
	
if "Sasha" not in test:
	print('Sasha is not in test')

test = []
test.append('Hi')
test.append(3) # в конец списка
test.append([1, 2])
print(len(test))
test.remove('Hi')
print(len(test))
test.insert(0, 'Hello') # вставляет на определенную позицию.
print(test)
test = [1, 2, 3, 4, 4, 4]
print( max(test) ) # min
print( test.count(4) )
test.reverse() #переворачивает писок
print(test)

def print_spam():
	print('Funtion')

print_spam()
print_spam()

def multiply(number):
	print(number * 2)

multiply(5)

def maxi(x, y):
	if x > y:
		return x
	else:
		return y

print(maxi(10,12))
# строки документирование
def say_hi():
	'''Qwerty'''
	print('Hello')
	
print(say_hi.__doc__)

say = say_hi
say()
# функции можно передать функцию!!! Урок 11

# модули
import random

print( random.randint(1,  100) )
for i in range(10):
	print( random.randint(1, 1000) )

from random import randint
print( randint(1, 10) )

from math import *
print( pi )
from math import sqrt as my_sqrt
