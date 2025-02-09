import math
from timeit import default_timer as timer

#Cортировка методом вставки

start = timer()

stepcounter = 0
def methodInsert(cabinet,to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global stepcounter
    while(check_location >= 0):
        stepcounter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = - 1
        check_location = check_location - 1
    stepcounter += 1
    cabinet.insert(insert_location, to_insert)
    return cabinet

cabinet = [1, 2, 3, 3, 4, 6, 8, 12]
new_cabinet = methodInsert(cabinet, 5)
print(new_cabinet)
print(stepcounter)

end = timer()
print(end - start)


def insertionSort(dataList):
    new_dataList = []
    global stepcounter
    while len(dataList) > 0:
        stepcounter += 1
        toInsert = dataList.pop(0)
        new_dataList = methodInsert(new_dataList, toInsert)
    return new_dataList

dataList = [8, 4, 5, 6, 1, 2, 3, 7, 145, 555, 17, 1288]
sorted_dataList = insertionSort(dataList)
print(sorted_dataList)
print(stepcounter)


#Сортировка слиянием (Делал по книге, Суть понятна, но не до конца понял этот метод именно в плане кода.
# На сколько я понял он является самым быстрым алгоритмом, поэтому хотелось бы проговорить его еще раз на паре)


def merging(oneList, secondList):
    thirtyList = []
    while(min(len(oneList),len(secondList)) > 0):
        if oneList[0] > secondList[0]:
            paste = secondList.pop(0)
            thirtyList.append(paste)
        elif oneList[0] <= secondList[0]:
            paste = oneList.pop(0)
            thirtyList.append(paste)
    if(len(oneList) > 0):
        for i in oneList:
            thirtyList.append(i)
    if (len(secondList) > 0):
        for i in secondList:
            thirtyList.append(i)
    return thirtyList


def splitMerge(list1):
    thirtyList = []
    if (len(list1) == 1):
        thirtyList = list1
    else:
        oneList = splitMerge(list1[:math.floor(len(list1)/2)])
        secondList = splitMerge(list1[math.floor(len(list1)/2):])
        thirtyList = merging(oneList, secondList)
    return thirtyList

list1 = [4, 1, 3, 2, 6, 3, 18, 2, 9, 7, 3, 1, 2.5, -9]
# oneList = [1, 3, 4, 4, 5, 7, 8, 9]
# secondList = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
thirtyList = splitMerge(list1)
print(thirtyList)

# метод Пузырьком


def bubbleMethod(mass):
    for run in range(len(mass) - 1):
        for l in range(len(mass) - 1):
            if mass[l] > mass[l + 1]:
                mass[l], mass[l + 1] = mass[l + 1], mass[l]
    return mass


mass = [5, 7, 4, 3, 8, 2, -1, 17, 139, 44]
new_mass = bubbleMethod(mass)
print(new_mass)
