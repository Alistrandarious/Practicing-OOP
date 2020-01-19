# print("Hello World!")  # functions use round brackets and can take parametres.

# Create function


def bark():
    print("I'm about to bark!")
    print("WOOF! " * 5)

bark()


def doubleSquare(x=0):
    square = x ** 2
    double = square * 2
    return double


print(doubleSquare(5))


def add(num1, num2):
    addition = num1 + num2
    return addition


add(3, 4)


def subtract(*multiargs):
    print(type(multiargs))
    print(multiargs)
    for x in multiargs:
        print(x)


def total(*multiargs): # * in the def is sum_total is a power character.
    sum_total = sum(multiargs)
    return sum_total

def maximum(*multiargs):
    max_x = max(multiargs)
    return max_x


print(add(69, 420))
print(total(1, 2, 3, 4, 5, 6, 7, 8, 9, 420))
print(maximum(435435, 345345345345, 3454353453453452514, 3, 53454354354354325, 235235))





