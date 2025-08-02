same = []
different = []
violations = 0

#get input

X = int(input())
for i in range(X):
    same.append(input().split())

Y = int(input())
for i in range(Y):
    different.append(input().split())

G = int(input())
name_to_group = {}

for id in range(G):
    group = input().split()
    for name in group:
        name_to_group[name] = id

for a,b in same:
    if name_to_group.get(a) != name_to_group.get(b):
        violations += 1

for a,b in different:
    if name_to_group.get(a) == name_to_group.get(b):
        violations += 1

print(violations)