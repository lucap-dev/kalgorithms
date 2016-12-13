# Insertion Sort algorithm


def insert(array, i):
    # store the current element
    key = array[i]

    # iterate over the sorted array
    for j in xrange(i - 1, -1, -1):
        if key < array[j]:
            array[j + 1] = array[j]
            array[j] = key
        else:
            break


def sort(array):
    for i in xrange(1, len(array)):
        insert(array, i)


if __name__ == "__main__":
    pass
