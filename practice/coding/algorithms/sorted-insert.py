import bisect

def sorted_insert_manual(arr: list[int], value: int) -> list[int]:
    """
    Insert value into sorted array maintaining order (manual implementation).

    arr: sorted list of integers
    value: integer to insert
    Returns: new sorted list with value inserted

    Time Complexity: O(n) - O(log n) for binary search + O(n) for insertion
    Space Complexity: O(1) - modifies in-place
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    arr.insert(left, value)
    return arr


def sorted_insert_bisect(arr: list[int], value: int) -> list[int]:
    """
    Insert value into sorted array maintaining order (using bisect).

    arr: sorted list of integers
    value: integer to insert
    Returns: new sorted list with value inserted

    Time Complexity: O(n) - O(log n) for binary search + O(n) for insertion
    Space Complexity: O(1) - modifies in-place
    """
    bisect.insort(arr, value)
    return arr


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9], 4, [1, 3, 4, 5, 7, 9], "Insert in middle"),
        ([1, 3, 5, 7, 9], 0, [0, 1, 3, 5, 7, 9], "Insert at beginning"),
        ([1, 3, 5, 7, 9], 10, [1, 3, 5, 7, 9, 10], "Insert at end"),
        ([], 5, [5], "Insert into empty array"),
        ([1, 2, 3], 2, [1, 2, 2, 3], "Insert duplicate"),
        ([5], 3, [3, 5], "Insert into single element"),
    ]

    print("Testing manual implementation:")
    for arr, value, expected, desc in test_cases:
        result = sorted_insert_manual(arr.copy(), value)
        print(f"  {desc}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"

    print("\nTesting bisect implementation:")
    for arr, value, expected, desc in test_cases:
        result = sorted_insert_bisect(arr.copy(), value)
        print(f"  {desc}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"

    print("\nAll tests passed! ✓")
