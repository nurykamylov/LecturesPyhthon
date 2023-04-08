# a = 3
# b = 11
# s = 2022
# print('a= ')
# print(type(a))
# print(a, b, s)
# print(a,'-',b,'-',s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'first - {a} second - {b} third - {s}')

# ##

# print('Введите первое число:')
# a = input()
# b = input('введите второе число: ')
# print('type of a+b:')
# print(type(a+b))
# print(a,'-',b,'=', a+b)
# a = int(a)
# b = int(b)
# print(f"{a}+{b} = {a+b} ") 

# ##

# n = '1.345'
# print(float(n) * 2)
# m = 2
# print(float(m))

# ##

# n = int(input('type the number: ')) # 5
# print(n * 2) # 10

## Rounding the numbers

# a = 1.43425
# b = 2.2983
# c = round(a * b, 5) # 3,29633
# print(c)

# ## Bools
# a = 1 > 4
# print(a) # False
# a = 1 < 4 and 5 > 2
# print(a) # True
# a = 1 == 2
# print(a) # False
# a = 1 != 2
# print(a) # True
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# a = 1 < 3 < 5 < 10
# print (a) # True

                                        # Conditions

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
"""
if condition1 and condition2: # выполнится, когда оба условия окажутся верными
#operator
if condition3 or condition4: # выполнится, когда хотя бы одно из условий
окажется верным
# operator
"""
n = int(input())
if n % 2 == 0 and n % 3 == 0:
    print('Число кратно 6')
if n % 5 == 0 and n % 3 == 0:
    print('Число кратно 15')

                                    # While Loop

'''
while condition:
# operator 1
# operator 2
# ...
# operator n
'''

n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10

else:
    print('Пожалуй')
    print('хватит )')
print(summa) # 9

#Задача: Пользователь вводит число, необходимо найти минимальный делитель данного числа
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2   
        print(n)
        flag = False
    i += 1

                                # Ranges

'''
for i in enumeration:
# operator 1
# operator 2
# ...
# operator n
'''

for i in 1, -2, 3, 14, 5:
    print(i)
# 1 -2 3 15 5

r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20

for i in 'qwerty':
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

                                
                                # Срезы

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок