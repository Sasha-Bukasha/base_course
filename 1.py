a = int(input('Давай первый отрезок: '))
b = int(input('Давай второй отрезок: '))
c = int(input('Давай третий отрезок: '))

if a <= b + c and c <= b + a and b <= a + c:
    print('Не, брат, так не льзя')
else:
    if a = b:
        if a = c:
            print('Равносторонний')
        else:
            print('Равнобедренный')
    else:
        print('Разносторонний')
