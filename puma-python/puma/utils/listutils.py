import copy

def getElementIndex(list, predict, index, countDefault):
    pos = 0
    count = 0
    for element in list:
        if pos >= index and predict(element):
            if countDefault == count:
                return pos
            else:
                count += 1
        else:
            pos += 1

    return -1


def getElementIndexFromIndex(list, predict, index):

    return getElementIndex(list, predict, index, 0)

def getElementIndexByCount(list, predict, countDefault):

    return getElementIndex(list, predict, 0, countDefault)


def getPermutation(list):

    res = []

    res.append([])

    for i in range(len(list)):

        current = []

        for l in res:

            j = 0

            while j < len(l) + 1:

                l.insert(j, list[i])
                temp = copy.deepcopy(l)
                current.append(temp)
                l.pop(j)

                j += 1
        res = copy.deepcopy(current)

    return res



