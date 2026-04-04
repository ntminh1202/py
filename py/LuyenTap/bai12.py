n = int(input("Nhập n: "))
_list = ['abc','xyz','aba','1221','i','i2','5yhy5']

count = 0
for i in _list:
    if len(i) >= n and i[0] == i[-1]:
        count += 1

print("Kết quả:", count)