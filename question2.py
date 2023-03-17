global arrayData
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(key):
    for i in range(len(arrayData)):
        if arrayData[i] == key:
            return True
    return False

def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData - 1)):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp


key = int(input("Input integer to search: "))
result = linearSearch(key)
if result == True:
    print("{} was successfully found".format(key))
else:
    print("Value not found")
