import sys
a = sys.stdin.readline()
b = sys.stdin.readline()
c = int(a) * int(b[2])
d = int(a) * int(b[1])
e = int(a) * int(b[0])
print(c)
print(d)
print(e)
print(c+(d*10)+(e*100))