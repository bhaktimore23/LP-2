def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
array = [7, 2, 5, 1, 8, 3]
sorted_array = selection_sort(array)
print(sorted_array)
