import random

def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value

    tries = 0
    num = None
    while num != target:
        it = random.randint(0, len(items) - 1)
        tries += 1
        num = items[it]
    print(f"it took {tries} tries to get target value")

    return it




def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.

    checks = 0
    for i in range(len(items)):
        checks += 1
        if items[i] == target:
            return (i, checks)
    return (-1, checks)




def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements binary search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.

    checks = 1
    minimum = 0
    maximum = len(items) - 1
    it = int((maximum + minimum) / 2)
    num = items[it]
    while num != target:
        if target < num:
            maximum = it - 1
        else:
            minimum = it + 1
        if maximum < minimum:
            return (-1, checks)
        it = int((maximum + minimum) / 2)
        checks += 1
        num = items[it]

    return (it, checks)