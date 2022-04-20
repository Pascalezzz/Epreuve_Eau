# format 12 34 == aa bb
for a in range(100):
    for b in range(a+1, 100):
        print(f"{a:02d} {b:02d},", end=" ")
        