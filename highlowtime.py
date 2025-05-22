n = int(input(""))
tides = input("")
tides = list(map(int, tides.split()))
tides.sort()
n = n//2

low = tides[:n]
low.sort(reverse = True)
high = tides[n:]

ordered = []

for i in range(n):
    ordered.append(low[i])
    ordered.append(high[i])

for i in range(n*2):
    x = ordered[i]
    print(x, end= ' ')
