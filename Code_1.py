def max_subarray_sum_and_length(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0

    for i in range(len(arr)):
        if current_sum <= 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    length = end - start + 1
    return max_sum, length

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4,9,11,22,-25]
max_sum, length = max_subarray_sum_and_length(arr)
print("Max subarray sum:", max_sum)
print("Number of elements in max subarray:",length)