# №1
a = int(input('Давай число: '))

if a % 2 == 0:
    print()
    print('Чётное число')
else:
    print()
    print('Нечётное число')

# №3
a = int(input('Давай год: '))

if a <= 0:
    print()
    print('Я отрицаю существование этого года')
elif a % 4 == 0:
    print()
    print('Високосный')
else:
    print()
    print('Невисокосный')

# №5
a = int(input('Давай целое число: '))
b = int(input('Давай второе целое число: '))

if b == 0:
    print()
    print('Делить на нуль пока нельзя :(')
elif a % b == 0:
    print()
    print(f'{a} делится на {b}', a / b)
else:
    print()
    print(f'{a} не делится на {b}', a % b)

# доп №1
a = int(input('Давай первый коэффициент: '))
b = int(input('Давай второй коэффициент: '))
c = int(input('Давай третий коэффициент: '))

D = b**2 - 4 * a * c

if D < 0:
    print()
    print('Нет корней')
elif D == 0:
    print()
    print('x =',b*(-1)/(2*a))
else:
    print()
    print('x1 =',(b*(-1)-(D**0.5))/(2*a))
    print('x2 =',(b*(-1)+(D**0.5))/(2*a))