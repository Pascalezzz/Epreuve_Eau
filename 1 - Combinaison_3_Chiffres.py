# format: 123 == abc
#a>b>c
for a in range(8):
	for b in range(a+1, 9):
	    for c in range(b+1, 10):
	        print(str(a)+str(b)+str(c), end =" ")