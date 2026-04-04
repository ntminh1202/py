f = open("test.txt", "r", encoding="utf-8")
n = int(input("n = "))
for i in range(n):
    print(f.readline(), end="")
f.close()