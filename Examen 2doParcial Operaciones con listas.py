calif = [8, 9, 7, 10, 6]

print(max(calif))
print(min(calif))
print(sum(calif))
prom = sum(calif) / len(calif)

calif.sort()
calif.sort(reverse=True)

top3 = calif[:3]
aprobados = [c for c in calif if c >= 6]