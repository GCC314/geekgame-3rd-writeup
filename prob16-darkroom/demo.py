a=[1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0][::-1]
b = ""
for i in range(0, len(a), 8):
    b += chr(int("".join(map(str, a[i:i+8])), 2))
print(b)
