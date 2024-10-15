array = [73,	-2,	-62,	-68,	58,	81,	38,	-34,	-21,	-51,	89,	73,	39,	-64,	-92]


def selectionshor(V, tam):
    for N in range(tam):
        menor = V[N]
        indice = N
        
        for i in range(N, tam):
            if V[i] < menor:
                menor = V[i]
                indice = i
        if menor != V[N]:
            aux = V[N]
            V[N] = V[indice]
            V[indice] = aux
    return V

print(selectionshor(array, len(array)))
        