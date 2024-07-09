import random
num = random.randint(0, 100)

print('Добро пожаловать в числовую угадайку')
print('Угадайте число от 0 до 100.')

def is_valid(n):
    if n.isdigit() and  0 < int(n) < 100:
        return True
    else:
        return False

while True:
    print('Введите число:')
    n = input()
    if is_valid(n) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if is_valid(n) == True:
        n = int(n)

        if n == num:
            print(f'Вы угадали, это число {n}, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif n > num:
            print('Слишком много, попробуйте еще раз')

            continue
        else:
            print('Слишком мало, попробуйте еще раз')
            continue