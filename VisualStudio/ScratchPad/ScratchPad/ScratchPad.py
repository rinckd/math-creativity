
class CounterClass(object):
    def __init__(self):
        self.counter = 0
    def add_counter(self):
        self.counter+=1
    def get_counter(self):
        return self.counter

a = CounterClass()

def factorial(n, a):
    if n <= 1:
        return 1
    a.add_counter()
    return n * factorial(n-1, a)


def fib(n, a):
    if n <= 3:
        return 1
    a.add_counter()
    return fib(n-1, a) + fib(n-2, a)





print (fib(10,a))
print (a.get_counter())
k = 0
