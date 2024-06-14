from algorithms.sorting.radix_sort import radix_sort, xidar_non_sort


def main() -> None:
    print(radix_sort([529, 531, 1223, 1736, 1936, 2007, 2016], 4))
    print(xidar_non_sort([529, 531, 1223, 1736, 1936, 2007, 2016], 4))


if __name__ == "__main__":
    main()
