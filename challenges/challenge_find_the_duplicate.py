def has_type_error(nums):
    for i in nums:
        if (type(i) != int or i < 0):
            raise TypeError


def has_duplicate(nums):
    for i in range(len(nums) - 1):
        if (nums[i] == nums[i + 1]):
            return nums[i]
    return False


def find_duplicate(nums):
    try:
        has_type_error(nums)
        merge_sort(nums, 0, len(nums))
        return has_duplicate(nums)
    except TypeError:
        return False


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
