def check_mod(num1: int, div: int) -> bool:
    return num1 % div == 0


def celebrate(test: bool) -> str:
    return"Hurray!"


print(check_mod(27, 3))
print(check_mod('six', 5))
print(celebrate(check_mod(3, 4)))
