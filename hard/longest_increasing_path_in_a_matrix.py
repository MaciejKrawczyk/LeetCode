def longest_increasing_path(matrix):
    """ leetcode 329. Longest increasing path in a matrix, used dfs algorithm and caching """

    def dfs(i, j):
        """ Helper function to perform depth-first search (DFS) from a given cell (i, j) """
        if memo[i][j] == 0:
            curr_val = matrix[i][j]
            up = dfs(i - 1, j) if i > 0 and curr_val > matrix[i - 1][j] else 0
            down = dfs(i + 1, j) if i < rows - 1 and curr_val > matrix[i + 1][j] else 0
            left = dfs(i, j - 1) if j > 0 and curr_val > matrix[i][j - 1] else 0
            right = dfs(i, j + 1) if j < cols - 1 and curr_val > matrix[i][j + 1] else 0

            memo[i][j] = 1 + max(up, down, left, right)
        return memo[i][j]

    # Check if the matrix is empty or contains no elements
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    # empty matrix for caching
    memo = [[0] * cols for _ in range(rows)]

    max_path_length = 0
    for i in range(rows):
        for j in range(cols):
            path_length = dfs(i, j)
            max_path_length = max(max_path_length, path_length)

    return max_path_length
