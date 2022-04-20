def Majuscule_Sur_Deux(string):
    if type(string) != str:
        print("error")
        exit()

    final_str = ""
    s = True
    for i in string:
        final_str += i.upper() if s else i.lower()
        if i.isalpha():
            s = not s
    return final_str

print(Majuscule_Sur_Deux("Hello World !"))