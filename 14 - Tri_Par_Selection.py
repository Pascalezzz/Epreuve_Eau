def Tri_Par_Selection(nombres):
    if type(nombres) != list:
        print("error")
        exit()
    
    if all(type(d) == int for d in nombres) == False:
        print("error")
        exit()

    for i in range(len(nombres)):
        min_idx = i
        for j in range(i+1, len(nombres)):
            if nombres[min_idx] > nombres[j]:
                min_idx = j
    
        nombres[i], nombres[min_idx] = nombres[min_idx], nombres[i]
        return(nombres)

nombres_liste = [64, 25, 12, 22, 11]
Tri_Par_Selection(nombres_liste)
print(nombres_liste)

nombres_liste = ["test", "test", "test"]
Tri_Par_Selection(nombres_liste)
print(nombres_liste)