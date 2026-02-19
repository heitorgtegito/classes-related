def seilaqporraeessa(L):
    print("Elemento        Índice")
    print("--------        ------")
    for i in range(len(L)):
        x = L[i]
        if x%2 == 0:
            print(f"{x}               {i}    ")

seilaqporraeessa([2, 1, -1, 8])
seilaqporraeessa([3, 1, -1, 5, 9, 13])