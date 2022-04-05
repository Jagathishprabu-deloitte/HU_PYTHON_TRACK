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
    def __init__(self):
        pass
    def pairs(self,list2):
        pair = list(combinations(list2, 2))
        return pair


value = "12314532"
obj = StringClass(value)
print(obj.length())
print(obj.tolist(value))
list2=obj.tolist(value)
obj2 = PairsPossible()
print(obj2.pairs(list2))