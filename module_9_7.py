def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res <= 0 or res == 1:
            print('Составное')
            return res
        for i in range(2, int(res) + 1):
            if res % i == 0:
                print('Составное')
                return res
            print('Простое')
            return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 6))

