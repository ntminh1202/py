f = open("test.txt", "w", encoding="utf-8")
f.write(input("Nhập đoạn văn: "))
f.close()

f = open("test.txt", "r", encoding="utf-8")
print(f.read())
f.close()