nums = [4,1,2,1,2]

# def is_single(nums):
#     duplicates = []
#     for i in range(len(nums)):
#         if nums[i] not in duplicates:
#             if nums.count(nums[i]) == 1:
#                 return nums[i]
#             else:
#                 duplicates.append(nums[i])

# Todo learn about this optimal solution...

def is_single(nums):
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
        print(nums)
    return nums[0]



print(is_single(nums))
