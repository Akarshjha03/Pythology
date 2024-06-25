'''Given a sorted array and a target value,return the index if the target is found. If not,return the index where it would be if 
it were inserted in order.'''

def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

#Use case:
nums = [1, 3, 5, 6]
target = 5
print("Array:", nums)
print("Target:", target)
print("Index:", search_insert(nums, target))  # Output: 2

target = 2
print("Array:", nums)
print("Target:", target)
print("Index:", search_insert(nums, target))  # Output: 1

target = 7
print("Array:", nums)
print("Target:", target)
print("Index:", search_insert(nums, target))  # Output: 4