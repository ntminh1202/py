f = open("demo_file1.txt", "w", encoding="utf-8")
f.write("Thuc\nhanh\nvoi\nfile\nIO")
f.close()

f = open("demo_file1.txt", "r", encoding="utf-8")
print(f.read().replace("\n", " "))
f.close()

f = open("demo_file1.txt", "r", encoding="utf-8")
for line in f:
    print(line, end="")
f.close()