from functools import reduce


class MapDictionary:
    list1 = ["Netflix", "Hulu", "Sling", "Hbo"]
    list2 = [198, 166, 237, 125]
    print("List1: ")
    print(list1)
    print("List2: ")
    print(list2)
    map_dict = dict(zip(list1, list2))
    print("Dictionary: ")
    print(map_dict)
    print()

class ReduceMultiply:
    list1 = []
    n = int(input("Enter number of elements in list:"))
    for i in range(0, n):
        ele = int(input("Enter value: "))
        list1.append(ele)
    print("List: ")
    print(list1)
    multiply = reduce(lambda a,b:a*b,list1)
    print("Multiplied Values: ")
    print(multiply)
    print()

class FilterMap:
    list1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
    print("List: ")
    print(list1)
    result = list(filter(lambda x: x > 0 , map(lambda x: x * -1, list1)))
    # result = list(map(lambda a: -1 * a, list(filter(lambda a: a < 0, list1))))
    # result = list(filter(lambda a : a < 0,list1))
    # result = list(map(lambda b : -1*b,result))
    print("Result: ")
    print(result)
    print()

