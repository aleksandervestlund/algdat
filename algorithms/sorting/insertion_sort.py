from typing import Any


def insertion_sort(arr: list[Any]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main() -> None:
    arr = [12, 11, 13, 5, 6, 7, 1, 2, 3, 4, 8, 9, 10]
    insertion_sort(arr)
    print(f"Sorted array is: {arr}")


if __name__ == "__main__":
    main()
