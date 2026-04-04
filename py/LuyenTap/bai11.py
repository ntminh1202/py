n = int(input("Nhập n: "))
_list = ['abc','hello','hi','python','code']

_new = []
for i in _list:
    if len(i) > n:
        _new.append(i)

print(_new)