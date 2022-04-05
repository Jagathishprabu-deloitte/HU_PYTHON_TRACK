from math import factorial

num1 = int(input("Enter Value: "))
for i in range(num1):
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end =" ")
    for j in range(num1-i-1):
        print(end="0 ")
    print()
print()

num2=int(input("Enter Value: "))
for i in range(num2):
    print(" "*(num2-i), "*"*(i*2+1))
    print()
for j in range(num2-2, -1,-1):
    print(" "*(num2-j), "*"*(j*2+1))
    print()
print()

num3=int(input("Enter Value: "))
temp=num3;
for i in range(num3):
    print(end=" "*(temp))
    if i==num3-1:
        print("*"*((2*num3)-1))
        break;
    for j in range(i+1):
        if j==0 or j==i:
            print(end="* ")
        else:
            print(end=" "*(2))
    temp=temp-1
    print()
print()

num4=int(input("Enter Value: "))
for i in range(num4):
    for j in range(num4):
        if i==0 or j==(num4-1) or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()