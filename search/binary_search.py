# Binary search module


def check_arguments(array, element):
    if array is None:
        raise TypeError

    if element is None:
        raise TypeError


def find(array, element):
    check_arguments(array, element)

    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:

        i = (min_index + max_index) / 2

        if array[i] == element:
            return i

        if array[i] > element:
            max_index = i - 1

        if array[i] < element:
            min_index = i + 1

    return -1


if __name__ == "__main__":
    pass
