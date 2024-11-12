def is_prime(num):
    n = 0
    for i in range(1, num + 1,):
        if num % i == 0:
            n += 1
            if n == 3:
                return False
    return True


print(is_prime(73))