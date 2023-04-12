strs = ["flower","flow","flight"]


def long(strs):
    length = len(min(strs))
    result = ''
    for i in range(length):
        for j in range(len(strs) - 1):
            if strs[j][i] != strs[j+1][i]:
                return result
        result += strs[0][i]

    return result

print(long(strs))