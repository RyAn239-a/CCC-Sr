N = int(input(""))
sums = 0

if N % 4 == 0:
    sums += 1
if N % 5 == 0:
    sums+=1
while N >= 9:
    N = N-4
    if N % 5 == 0:
        sums+=1

print(sums)
