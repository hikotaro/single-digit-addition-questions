import random


value1 = random.randint(0, 9)
value2 = random.randint(0, 9)
answer = value1 + value2

num = int(input(f'{value1} + {value2} = '))

if answer == num:
    print('正解!')
else:
    print(f'不正解! 正解は {answer} です')
