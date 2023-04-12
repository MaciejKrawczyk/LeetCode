n = 1


def happy(n):
    loop_values = []
    while n != 1:
        n = sum([int(i)*int(i) for i in str(n)])
        if n in loop_values:
            return False
        loop_values.append(n)
    return True


print(happy(n))
