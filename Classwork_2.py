""" 1.Створити список цілих чисел, які вводяться з терміналу та визначити серед них
максимальне та мінімальне число"""

numbers=[]
length=int(input("Input length: "))
numbers=[int(input("Enter number: ")) for i in range(length)]
print(numbers)
print(max(numbers))
print(min(numbers))

""" 2.В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3"""

interval = list(range(11))
print(interval)
print("парні, які діляться на 2:")
for i in range(10):
    if interval[i]%2 == 0:
        print(interval[i])
        
print("непарні, які діляться на 3:")
for i in range(10):
    if interval[i]%3 == 0 and interval[i]%2!=0:
        print(interval[i])

print("числа, які не діляться на 2 та 3:")
for i in range(10):
    if interval[i]%3!= 0 and interval[i]%2!=0:
        print(interval[i])

""" 3.Написати програму, яка обчислює факторіал числа, яке користувач вводить
(не використовувати рекурсивного виклику функції)"""

fact=1
num=int(input("Enter number: "))
for i in range(num):
    while num!=1:
        fact*=num
        num=num-1

""" 4.Напишіть скрипт, який перевіряє логін, який вводить користувач
Якщо логін вірний (First), то привітайте користувача. 
Якщо ні, то виведіть повідомлення про помилку"""

user_id=(input("User id: "))
if user_id == "First":
    print("Welcome!")
else:
    print("Error: Go away") 

""" 5.Перший випадок. 
Написати програму, яка буде зчитувати числа поки не зустріне від’ємне
число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється)"""

number = (int(input("number: ")))
while number > 0:
    print(number)
    number = (int(input("number: ")))


"""7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
(наприклад 10 equals 2 * 5
                    11 is a prime number
                    12 equals 2 * 6
                    13 is a prime number
                    14 equals 2 * 7
                     ………………….)"""

for number_to_check in range(10, 31):
    i = 2
    limit = int(math.sqrt(number_to_check))
    while i <= limit:
        if number_to_check % i == 0:
            print(f'Number {number_to_check} is equal to 2 * {number_to_check / 2}')
            break
        i += 1
    else:
        print(f'Number {number_to_check} - simple')

"""8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)"""
sentence = """Gimme, gimme, gimme a man after midnight
            Won't somebody help me
            Chase the shadows away
            Gimme, gimme, gimme a man after midnight
            Take me through the darkness
            To the break of the day"""
sorted_sentence = [word for word in sorted(sentence.split(), key=lambda a: len(a))]
print(sorted_sentence)