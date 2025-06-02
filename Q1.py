def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur):
    n = len(cols)
    if i == n:
        return True

    for j in range(n):
        if cols[j] or rightDiagonal[i + j] or leftDiagonal[i - j + n - 1]:
            continue

        cols[j] = 1
        rightDiagonal[i + j] = 1
        leftDiagonal[i - j + n - 1] = 1
        cur.append(j + 1)

        if placeQueens(i + 1, cols, leftDiagonal, rightDiagonal, cur):
            return True

        cur.pop()
        cols[j] = 0
        rightDiagonal[i + j] = 0
        leftDiagonal[i - j + n - 1] = 0

    return False

def nQueen(n):
    cols = [0] * n
    leftDiagonal = [0] * (n * 2)
    rightDiagonal = [0] * (n * 2)
    cur = []

    if placeQueens(0, cols, leftDiagonal, rightDiagonal, cur):
        return cur
    else:
        return [-1]

if __name__ == "_main_":
    n = 4
    ans = nQueen(n)
    print(" ".join(map(str, ans)))