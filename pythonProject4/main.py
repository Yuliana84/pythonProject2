p = 0
while True:
    try:
        q = input('Сколько билетов вы бы хотели приобрести? ')
        q = int(q)
        if type(q) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(q):
    i += 1
    while True:
        try:
           a = input(f'Для какого возраста билет №{i}? ')
           a = int(a)
           if a < 18:
                print('Билет бесплатный')
           elif 25 > a >= 18:
                p += 990
                print('Стоимость билета: 990 руб.')
           else:
                p += 1390
                print('Стоимость билета: 1390 руб.')
           if type(a) == int:
                break
        except ValueError:
            print('Введите целое число')
if q > 5:
    p = p - ((p / 100) * 10)
    print(f'Сумма к оплате {p} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 5-и человек')
else:
    print(f'Сумма к оплате {p} руб.')
