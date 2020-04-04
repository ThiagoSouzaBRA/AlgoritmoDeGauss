import numpy as np

def multVetor(v, x):
    m1 = []
    for i in range(len(v)):
        m1 += [v[i] * x]
    return m1


def SomaVetor(v1, v2):
    m1 = []
    for i in range(len(v1)):
        m1 += [v1[i] + v2[i]]
    return m1


def Swap(A, i, j):
    m1 = []
    m2 = []
    for ix in range(len(A) + 1):
        m1 += [A[j][ix]]
        m2 += [A[i][ix]]
    A[i] = m1
    A[j] = m2


def pivotamento(Matriz):
    #"Complexidade: O(n³), Há dois loops que o tornam a complexidade O(n²) entretanto é possivel que tenha um 3 loop então estimo O(n³)."
    for x in range(len(Matriz) - 1):
        for y in range(x + 1, len(Matriz)):
            recebe1 = Matriz[y][x]
            if recebe1 == 0:
                for k in range(x, len(Matriz)):
                    if Matriz[k][x] != 0:
                        Swap(Matriz, x, k)
                        recebe1 = Matriz[y][x]
            recebe2 = Matriz[x][x]
            if recebe2 == 0:
                continue
            div = recebe1 / recebe2
            Matriz[y] = SomaVetor(multVetor(Matriz[x], -div), Matriz[y])
    return Matriz


A = [[1, -1, 3, 2], [3, -3, 1, -1], [1, 1, 0, 3]]

print("\nMatriz :", np.matrix(A))
print("\nGauss :\n", np.matrix(pivotamento(A)))



