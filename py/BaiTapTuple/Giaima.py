
bang_ma = {'a':'!', 'b':'@', 'c':'#', 'd':'$'}
giai_ma = {v:k for k,v in bang_ma.items()}

s = input("Nhập chuỗi: ")

mahoa = ""
for i in s:
    mahoa += bang_ma.get(i, i)

giaima = ""
for i in mahoa:
    giaima += giai_ma.get(i, i)

print("Mã hóa:", mahoa)
print("Giải mã:", giaima)