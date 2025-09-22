if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    totalSwaps = 0  # To keep track of total swaps

    for i in range(n):
        numberOfSwaps = 0

        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps += 1
                totalSwaps += 1

        # If no elements were swapped during a traversal, array is sorted
        if numberOfSwaps == 0:
            break

    print(f"Array is sorted in {totalSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
