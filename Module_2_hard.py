def password(num):
    password = ''
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            if num % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input('Введите число из первой вставки (от 3 до 20): ', ))
result = password(n)
print('Пароль для второй вставки: ', result)








