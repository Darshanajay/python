def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements starting from 0 to n-1
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
a = [7, 9, 2, 6, 5, 3]
selection_sort(a)

print("Sorted array:", a)