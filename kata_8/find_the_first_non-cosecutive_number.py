def first_non_consecutive(arr):
    for i, num in enumerate(arr):
        if i+arr[0]!=num:
            return num