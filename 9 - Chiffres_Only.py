string_example="444333"

count=0
for l in string_example:
    if 48 <= ord(l) <= 57:
       pass
    else:
        count+=1
if count>0:
    print("false")
    exit()
else:
    print("true")