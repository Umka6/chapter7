
# code = input('Введите код:')
# if code == taalaicode:
#     a = input()
#     if a == password

a = int(input('Введите количество братьев и сестер:'))
b = int(input('Введите число яблок:'))

if b % a == 0:
    print('Дать')
elif b % a != 0:
    print("Съешь сам")
else:
    print('Не давай')
