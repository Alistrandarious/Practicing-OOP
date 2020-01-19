def add(num1, num2):
    return num1 +num2

addition = lambda num1, num2: num1 + num2 # has to be on one line, no statements or assignments, very simple - inputs and
# outputs. Never use on its own. Useful when combined with other functions.

print(add(2, 2))
print(addition(2, 2))


savings = [265, 700, 1000]
bonus = [x * 1.1 for x in savings]

print(bonus)

bonusL = list(map(lambda x: x * 1.1, savings)) #List = turns into a list. #Map = maps an object that is yet seen, object
                                                                            # with a set of instructions Whenever it's ready.

print(bonusL)

names = ["Harrison", "Barrison", "Jarrison"]
NAMES = list(map(lambda x: x.upper(), names))

print(NAMES)

for x in NAMES:
    print(x)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = lambda x: x % 2 == 0 # is remainder true or false?

print(list(map(lambda x: x % 2 == 0, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Use filter and Lambda to keep only purely numeric strings from a list.

my_list = ["Ali", "2.3454", "#1", "jdjofw23423", "4000000"]
print(list(filter(lambda x: x.isalpha(), my_list)))
print(list(filter(lambda x: x.isalnum(), my_list)))
print(list(filter(lambda x: x.isnumeric(), my_list)))


moreNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greaterThan = map(lambda spaghetti: spaghetti**2, moreNums) #this can be put into the "my_list" clause as a list

print(list(filter(lambda meatballs: meatballs > 30, map(lambda spaghetti: spaghetti**2, moreNums))))
#anything done more than once just use as a regular function. 

