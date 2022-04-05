from itertools import combinations


class StringClass:
    def __init__(self, value):
        self.str = value

    def length(self):
        return len(self.str)

    def tolist(self, value):
        list1 = list(value)
        return list1


class PairsPossible(StringClass):
    def __init__(self,value):
        self.str = value
    def pairs(self):
        pair = list(combinations(self.str, 2))
        return pair

class SearchCommonElements(StringClass):
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2

    def commonElements(self):
        removed = list(set(self.str1) & set(self.str2))
        return removed
1
class EqualSumPairs():
    def count(self, list1):
        list2 = []
        for i in list1:
            sum = 0
            for j in i:
                sum += int(j)
            list2.append(sum)
        return len(set(list2))



value1 = input("Enter String: ")
obj1 = StringClass(value1)
print("Length of the String: ")
print(obj1.length())
print("List of String: ")
print(obj1.tolist(value1))

value2 = input("Enter String: ")
obj2 = PairsPossible(value2)
list1=obj2.pairs()
print("Pairs Possible are: ")
print(list1)

obj3=SearchCommonElements(value1,value2)
print("Common Elements are: ")
print(obj3.commonElements())

obj4 = EqualSumPairs()
length=obj4.count(list1)
print("Count of unique sums: ")
print(length)
