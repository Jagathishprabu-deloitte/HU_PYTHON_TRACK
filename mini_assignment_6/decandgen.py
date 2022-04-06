def fib(n):
    a = 0
    b = 1
    if n == 1:
        # print(a)
        yield a
    else:
        # print(a)
        yield a
        # print(b)
        yield b
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            yield c


def smart_multiply(func):
    def inner(num1, num2):
        print("The Multiplication of", num1, "and", num2, "are", num1 * num2)
        num1, num2 = num2, num1
        return func(num1, num2)
    return inner

@smart_multiply
def multiply(num1, num2):
    print("The Multiplication of", num1, "and", num2, "are", num1 * num2)



n = int(input("Enter the value of n : "))
values = fib(n)
print(values)
print("The list of the first", n, " Fibonacci numbers are ")
for i in values:
    print(i)
print()



a = int(input("Enter the value of num1 : "))
b = int(input("Enter the value of num2 : "))
multiply(a,b)