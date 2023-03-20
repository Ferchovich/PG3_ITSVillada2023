def findNumber(numberArray: list, number: int | float):
    for index, value in enumerate(numberArray):
        if value == number:
            return index
    return None


array = [1,12,16,23]

print(f"El elemento se encuenta en el índice: {findNumber(array, 1)}")



