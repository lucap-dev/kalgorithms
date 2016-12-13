# Selection Sort algorithm


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def index_of_minimum(array, i):
    if array is None or len(array) == 0:
        raise IndexError

    tmp_min_i = i

    if i < len(array):
        for j in xrange(i + 1, len(array)):
            if array[j] < array[tmp_min_i]:
                tmp_min_i = j
    return tmp_min_i


def sort(array):
    if len(array) == 0:
        return

    for i in xrange(len(array)):
        j = index_of_minimum(array, i)
        swap(array, i, j)


if __name__ == "__main__":
    pass
