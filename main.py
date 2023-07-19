r = int(input())
c = int(input())
A = []
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    A.append(row)
transpose = []
for j in range(c):
    transposed_row = []
    for i in range(r):
        transposed_row.append(A[i][j])
    transpose.append(transposed_row)
for row in transpose:
    n=row[::-1]
    print(n)
