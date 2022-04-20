def Index_Wanted(string):
    string_list_all=string.split()
    string_list=string_list_all[:-1]
    string_list_search=string_list_all[-1]
    if string_list_search in string_list:
        print(string_list.index(string_list_search))
    else:
        print("-1")




Index_Wanted("Ceci est le monde qui contient Charlie un homme sympa Charlie")
Index_Wanted("test test test")
Index_Wanted("test boom")