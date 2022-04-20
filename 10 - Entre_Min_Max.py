def Entre_Min_Max(min=None, max=None):
    if type(min) != int or type(max) != int:
        print("erreur")
        exit() 

    if min>max:
        Entre_Min_Max_Swap(min, max)
        return
    for i in range(min, max):
        print(i, end=" ")

def Entre_Min_Max_Swap(min, max):
    max_bis=min
    min=max
    for i in range(min, max_bis):
        print(i, end=" ")

Entre_Min_Max(20, 25)
print("")
Entre_Min_Max(25, 20)
print("")
Entre_Min_Max("hello")