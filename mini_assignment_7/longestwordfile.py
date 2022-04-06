
with open("filereader.txt",mode="w") as file:
    str = input("Enter the words: ")
    file.write(str)
    file.close()

def longest_words(filereader):
    with open(filereader, 'r') as x:
        words = x.read().split()
    print("Given Words: ")
    print(words)
    max_len = len(max(words, key=len))
    max_length_word = list(filter(lambda x: len(x) == max_len, words))
    print("Longest Words in the File:")
    return max_length_word

class LongestWord:
    print(longest_words('filereader.txt'))



class Error(Exception):
    """Base class for other exceptions"""
    pass

class ExpressionTooSmallError(Error):
    """The input expression is too small"""
    pass

class ExpressionTooLargeError(Error):
    """The input expression is too large"""
    pass

class OperationError(Error):
    """Incorrect expression"""
    pass

class ErrorHandling:
    while True:
        eqn = input("Enter the expression to be solved : ")
        if eqn == "quit":
            break
        values = eqn.split()
        print(values)
        try:
            if len(values) < 3:
                raise ExpressionTooSmallError
            if len(values) > 3:
                raise ExpressionTooLargeError
            float_value1 = float(values[0])
            float_value2 = float(values[2])
            operation = values[1]
            if operation != '+' and operation != '-':
                raise OperationError
            if float_value1 and float_value2 and operation == "+":
                print("Result : ", float_value1, operation, float_value2, "=", float_value1 + float_value2)
            elif float_value1 and float_value2 and operation == "-":
                print("Result : ", float_value1, operation, float_value2, "=", float_value1 - float_value2)
            else:
                raise ValueError
        except ExpressionTooSmallError:
            print("The given expression is too small. Try giving inputs like (1 + 1)")
        except ExpressionTooSmallError:
            print("The given expression is too large. Try giving inputs like (1 + 1)")
        except OperationError:
            print("Enter operation as '+' or '-' ")
        except ValueError:
            print("The given value is not a number")
