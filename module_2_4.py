numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Дано
is_prime = True # Объявление переменной-флага
# Объявление списков для заполнения
primes = []
not_primes = []
# Цикл для перебора элементов списка numbers и заполнения списков primes и not_primes
for i in numbers:
    for j in range(2,i):
        is_prime = i % j > 0
        if i % j == 0:
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
# Вывод составленных списков на консоль
print (f'Primes: {primes}')
print (f'Not Primes {not_primes}')
