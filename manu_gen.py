def is_prime(n):
    if n == 3 or n == 2:
        return True
    for i in range(2, n):
       if n % i == 0:
           return False
    return True

def check(n):
    if n > 3 and n!= 5 and (n%2 == 0 or n%3 == 0 or n%5 == 0) :
        return False
    return True

def manipulate_generator(generator, n):
    # while is_prime(n +1):
    #     generator.send(n +1)
    #     n += 1
    if is_prime(n +1):
        generator.send(None)
        manipulate_generator(generator, n +1)


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        # print("X = {}".format(x))
        if x is not None:
            n = x
        else:
            n += 1
        # print("N = {}".format(n))
            

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
