def Trier_ASCII(list_a_trier):
    list_check = isinstance(list_a_trier, list)
    if list_check:
        list_a_trier.sort()
        print(list_a_trier)
    else:
        print("error")
        
list_string = ["Alfred", "Momo", "Gilbert"]
Trier_ASCII(list_string)
list_string = [1, 6, 4, 9]
Trier_ASCII(list_string)
list_string = "hello"
Trier_ASCII(list_string)