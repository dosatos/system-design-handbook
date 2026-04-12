import bisect

def binary_search_manual(arr: list[int], target: int) -> int:
    """
    Binary search implementation (manual iterative).
    Returns index of target if found, -1 otherwise.

    arr: sorted list of integers
    target: value to find
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(arr: list[int], target: int) -> int:
    """
    Binary search using bisect module.
    Returns index of target if found, -1 otherwise.

    arr: sorted list of integers
    target: value to find
    """
    idx = bisect.bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13], 7, 3, "Target exists"),
        ([1, 3, 5, 7, 9, 11, 13], 6, -1, "Target doesn't exist"),
        ([], 5, -1, "Empty array"),
        ([5], 5, 0, "Single element (found)"),
        ([1, 3, 5, 7, 9], 1, 0, "Target at beginning"),
        ([1, 3, 5, 7, 9], 9, 4, "Target at end"),
    ]

    print("Testing manual implementation:")
    for arr, target, expected, desc in test_cases:
        result = binary_search_manual(arr, target)
        print(f"  {desc}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"

    print("\nTesting bisect implementation:")
    for arr, target, expected, desc in test_cases:
        result = binary_search(arr, target)
        print(f"  {desc}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"

    print("\nAll tests passed! ✓")
