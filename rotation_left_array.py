# example
# move: 3
# arr : [2, 3, 4, 5, 6, 7]

# result: [5, 6, 7, 2, 3, 4]


# move one
# result partial: [3, 4, 5, 6, 7, 2]

# move two
# result partial: [4, 5, 6, 7, 2, 3]

# move Three
# result partial: [5, 6, 7, 2, 3, 4]


def rotationLeftArray(move, arr):
    tam = len(arr)
    moveLeft = move % tam
    if moveLeft == 0 or tam == moveLeft:
        return arr

    indexBase = moveLeft

    if indexBase == tam / 2:
        i = 0
        while indexBase < tam:
            saveDataIndex = arr[indexBase]
            arr[indexBase] = arr[i]
            arr[i] = saveDataIndex
            indexBase += 1
            i += 1
    else:
        count = 0
        while indexBase < tam and count < tam:
            index = indexBase
            first = True
            saveDataIndex = arr[index]
            while index != indexBase or first:
                first = False
                newIndex = index - moveLeft
                if newIndex < 0:
                    newIndex += tam
                saveDataNewIndex = arr[newIndex]
                arr[newIndex] = saveDataIndex
                saveDataIndex = saveDataNewIndex
                count += 1
                index = newIndex

            indexBase += 1

    return arr
