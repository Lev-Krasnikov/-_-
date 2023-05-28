import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

print('Сейчас мы поможем вам сгенерировать пароль')
print('Количество паролей для генерации:', end='')
col = int(input())

print('Длину одного пароля:', end='')
dlina = int(input())

print('Включать ли цифры 0123456789?')
if input().lower() == 'да':
    chars += digits

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
if input().lower() == 'да':
    chars += uppercase_letters

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
if input().lower() == 'да':
    chars += lowercase_letters

print('Включать ли символы !#$%&*+-=?@^_?')
if input().lower() == 'да':
    chars += punctuation


def generate_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    return password


for _ in range(col):
    print(generate_password(dlina, chars))