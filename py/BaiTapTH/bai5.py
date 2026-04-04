s = "Dem so luong tu xuat hien abc abc abc 12 12 it it eaut"
d = {}

for w in s.split():
    d[w] = d.get(w, 0) + 1

print(d)