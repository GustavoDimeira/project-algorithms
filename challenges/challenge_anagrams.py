def is_anagram(first_string, second_string):
    first_array = []
    second_array = []
    for letter in first_string:
        first_array.append(letter.lower())
    for letter in second_string:
        second_array.append(letter.lower())

    merge_sort(first_array, 0, len(first_array))
    merge_sort(second_array, 0, len(second_array))

    is_empty = first_string == "" or second_string == ""

    return (
        "".join(first_array),
        "".join(second_array),
        first_array == second_array and not is_empty
        )


def merge_sort(string, start, end):
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1
