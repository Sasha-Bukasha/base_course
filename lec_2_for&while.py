# for

for i in 1,3,4:
    print(i**2, end='xex')

print('')

for i in 1,3,4:
    print(i**2, end='\n') # \n - литер (переносит текст на нов строку то есть ставит ентер)

for i in 1,3,4:
    print(i**2, end=' - ') # ' - ' аргумент-сепаратор (заменяет "," в for на другой знак)



# While

'''i = i += 1

while i < 15:
    print('i - ',i)'''

for symbol in 'hello world':
    if symbol == 'o':
        continue
    print(symbol)