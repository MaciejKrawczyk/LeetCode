height = [1,8,6,2,5,4,8,3,7]


# Todo didn't pass all tests, need to eliminate one loop


def area(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            if height[i] <= height[j]:
                area = height[i] * (j-i)
            else:
                area = height[j] * (j-i)
            if area > max_area:
                max_area = area
    return max_area


print(area(height))
