
f = open("setInfo.txt", "w", encoding="utf-8")
f.write(input("Tên: ")+"\n")
f.write(input("Tuổi: ")+"\n")
f.write(input("Email: ")+"\n")
f.write(input("Skype: ")+"\n")
f.write(input("Địa chỉ: ")+"\n")
f.write(input("Nơi làm việc: ")+"\n")
f.close()

# đọc lại
f = open("setInfo.txt", "r", encoding="utf-8")
print(f.read())
f.close()