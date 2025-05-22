n = int(input(""))
swifts = input("")
swifts= list(map(int, swifts.split()))
semaphores = input("")
semaphores = list(map(int, semaphores.split()))
w = 0
e = 0
k = 0

for i in range(n):
    w = w + int(swifts[i])
    e = e + int(semaphores[i])
    if w == e:
        k = i + 1

print(k)