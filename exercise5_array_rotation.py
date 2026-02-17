def print_array(name, arr):
    print(f"{name}: {arr}")


# a) Using temporary array

def rotate_temp_array(nums, k):
    n = len(nums)
    k = k % n 
    if k == 0: return nums
    return nums[n-k:] + nums[:n-k]


# b) Rotate one by one

def rotate_one_by_one(nums, k):
    n = len(nums)
    k = k % n
    if k == 0: return
    
    for _ in range(k):
        last = nums[-1]

        for i in range(n-1, 0, -1):
            nums[i] = nums[i-1]
            
        nums[0] = last


# c) Reverse segments method

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate_reverse(nums, k):
    n = len(nums)
    k = k % n
    if k == 0: return

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
