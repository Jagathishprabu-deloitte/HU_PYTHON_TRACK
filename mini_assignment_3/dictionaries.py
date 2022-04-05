class FindDuplicates:
    def find_duplicates(self):
        a = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
        print(a)
        for i in range(len(a)):
            res = dict((x, a[i].count(x)) for x in set(a[i]))
            res = {key: val for key, val in res.items() if val != 1}
            print(res)


obj = FindDuplicates()
obj.find_duplicates()
print()


class MergeLists:
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    print(list1)
    print(list2)
    res = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            joinedlist = list1[i] + list2[j]
            res.append(joinedlist)
    print(res)
    print()


class InsertInto:
    list2 = ["h", "i", "j"]
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    print(list1)
    print(list2)
    for i in range(len(list2)):
        list1[2][1][2].append(list2[i])
    print(list1)
    print()


class MapDictionary:
    keys = ['red', 'blue', 'pink']
    values = [10, 20, 30]
    print(keys)
    print(values)
    map_dict = dict(zip(keys, values))
    print(map_dict)
    print()


class MergeDict:
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    print(dict1)
    print(dict2)
    dict1.update(dict2)
    print(dict1)
    print()


class RenameKey:
    givenDictionary = {"name": "Kelly",
                       "age": 25,
                       "salary": 8000,
                       "city": "New york"}
    print(givenDictionary)
    givenDictionary['location'] = givenDictionary.pop('city')
    print(givenDictionary)
    print()


class DicToList:
    dictionary_data = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
    print(dictionary_data)
    list_value = []
    for key, val in dictionary_data.items():
        list_value.append([key] + val)
    print(list_value)
    print()
