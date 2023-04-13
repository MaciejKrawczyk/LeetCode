heights = [5,1,2,3,4]


def check(heights):
    s = sorted(heights)
    res = 0
    for i, j in zip(heights, s):
        if i != j:
            res += 1
    return res


print(check(heights))
