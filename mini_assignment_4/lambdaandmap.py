
class LambdaEqn:
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))
    x = int(input("Enter value for x: "))
    print("The value for ax^2+bx+c is: ")
    eqn = lambda a,b,c,x : print(((a*x)*(a*x))+(b*x)+c)
    eqn(a,b,c,x)
print()

class CountOfA:
    list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
    print(list1)
    list2 = list(map(lambda word: word.count("a"), list1))
    print("Number of 'a' :")
    print(list2)
    list3 = list(map(lambda word: word.count("A"), list1))
    print("Number of 'A' :")
    print(list3)
    list4 = list(map(lambda word: word.count("a")+word.count("A"), list1))
    print("Number of 'a' and 'A':")
    print(list4)