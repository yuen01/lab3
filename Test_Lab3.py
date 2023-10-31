import Lab3

print("Test_Lab3")

def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_large_input():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 5, 8, 7, 2]
    result = Lab3.bubble_sort(input_arr, "SORT_ASCENDING")
    assert result == 1

def check_integers_in_array(arr):
    count = 0
    for item in arr:
        if isinstance(item, int):
            count += 1
    if count >= 10:
        return 1
    else:
        return 0

def test_check_integers_in_array():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 5, 8, 7, 2]
    result = check_integers_in_array(input_arr)
    print(result)

def check_integers_in_array2(arr):
    count = 0
    for item in arr:
        if isinstance(item, int):
            count += 1
    if count == 0:
        return 0
    else:
        return 1

def test_check_integers_in_array2():
    input_arr = []
    result = check_integers_in_array2(input_arr)
    print(result)


def check_integers_in_array3(arr):
    for item in arr:
        if not isinstance(item, int):
            return 2
    return 1
def test_check_integers_in_array3():
    input_arr = [64, 34, 25, 12, 22, 11,"test", 5, 8, 7, 2]
    result = check_integers_in_array3(input_arr)
    print(result)