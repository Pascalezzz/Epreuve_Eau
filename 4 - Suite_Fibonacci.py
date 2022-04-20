n_eme = int(input("Suite jusqu'au combientième chiffre ? "))

n1 = 0
n2 = 1
count = 0

#Si négatif
if n_eme <= 0:
   print("-1")

#Si 1
elif n_eme == 1:
   print(n1)

else:
   while count < n_eme:
       print(n1, end="")
       print("")
       n_e = n1 + n2
       n1 = n2
       n2 = n_e
       count += 1