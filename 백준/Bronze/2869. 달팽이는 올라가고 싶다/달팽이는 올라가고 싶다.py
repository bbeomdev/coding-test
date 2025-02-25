import sys
import math
a,b,v = map(int, input().split())
clim = a-b
print(math.ceil((v-b) / (a-b)))