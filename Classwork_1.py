""" 1.Роздрукувати всі парні числа менші 100"""
##while
# start = 0
# finish = 100
# i = 0
# while start < finish:
#     print(start)
#     start+=2
##for
# for j in range(2,100,2):
#   print (j)

""" 2.Роздрукувати всі непарні числа менші 100"""
# odd number
# for j in range(1,100,2):
#     print (j)

# odd number continue

# for val in range(100):
#     if val %2 == 0:
#         continue
#     print(val)

""" 3.Перевірити чи список містить непарні числа"""
# my_list=[6,8,4,6,5,88,7,56,61,24,25,31]
# for val in my_list:
#     if val %2 == 1:
#         print('first odd number',val)
#         break

""" 4.Створити список, який містить елементи цілочисельного типу, 
потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою"""
# my_list=[1,2,3,4,5,6,7,8]
# for i in range(len(my_list)):
#     my_list[i]=float(my_list[i])
# print(my_list)

""" 5.Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли"""
# my_list= [1,1]
# n=int(input())
# if n == 1:
#     print(1)
# else:
#     for j in range (2,n):
#         my_list.append(my_list[-1]+my_list[-2])
#     print(my_list)

""" 6.Створити список, що складається з чотирьох елементів типу string. 
Потім, за допомогою циклу for, вивести елементи по черзі на екран"""
# my_list = 'a','b','c','d'
# for val in my_list:
#     print(val)

""" 7.Змінити попередню програму так, щоб в кінці кожної букви елементів
 при виводі додавався певний символ, наприклад '#' """
# my_list = 'a','b','c','d'
# for val in my_list:
#     print(val,"#")

""" 8.Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне"""

# user_number = int(input("User number: "))
# num = 2
# while user_number % num !=0:
#     num += 1
# if num == user_number:
#     print('Prime number\n')
# else:
#     print('Not prime number\n')


""" 9.Знайти максимальну цифру дійсного числа"""
# Дійсне число генеруємо випадковим чином за допомогою методу random() з модуля random
# from random import random
# number = list(str(int(random()*100)))
# print(number)
# if int(number[0])>int(number[1]):
#     print(number[0])
# else:
#     print(number[1])

""" 10.Визначити чи введене слово паліндром, тобто чи воно читається однаково зліва направо і навпаки."""
# user_word = input("User word: ")
# reversed_word = ''.join(reversed(user_word))
# print(user_word,reversed_word)
# if user_word == reversed_word:
#     print('Palindrom')
# else:
#     print('Not palindrom')