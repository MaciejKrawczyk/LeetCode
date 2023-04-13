x = 10

# def sqrt(x):
#     i = 2
#     if x == 1:
#         return 1
#     elif x == 0:
#         return 0
#     while True:
#         if i*i > x:
#             return i-1
#         else:
#             i += 1


def sqrt(x):
    if x == 0:
        return 0
    first, last = 1, x
    while first <= last:
        mid = first + (last - first) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            last = mid - 1
        else:
            first = mid + 1
    return last


print(sqrt(x))
