
def esStep(number:int):
    numberToString = str(number)
    cant = 0
    for i in range(len(numberToString)):
        if i != (len(numberToString) - 1):
            if abs(int(numberToString[i]) - int(numberToString[i+1])) == 1:
                cant += 1

    return cant == len(numberToString) - 1 

print(esStep(12321))