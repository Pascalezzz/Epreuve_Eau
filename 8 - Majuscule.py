def capitalize_each_word(original_str):
    if type(original_str) != str:
        print("error")
        exit()
        
    result = ""
    list_of_words = original_str.split()
    for elem in list_of_words:
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
    print(result)
            
capitalize_each_word("bonjour mathilde, comment vas-tu ?!")
capitalize_each_word(42)
