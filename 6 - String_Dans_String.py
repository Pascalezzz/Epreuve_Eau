def string_dans_string(string="", substring=""):
    if type(substring) != str or type(string) != str:
        print("erreur")
        exit()

    if substring in string:
        print("True")
    else:
        print("False")


string_dans_string("bonjour", "jour")
string_dans_string("bonjour", "joure")
string_dans_string(42)