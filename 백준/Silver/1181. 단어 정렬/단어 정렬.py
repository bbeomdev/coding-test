n = int(input())
s_dict = {}
for i in range(n):
    s = input()
    s_dict[s] = len(s)
s_dict2 = {key: [] for key in sorted(s_dict.values())}
for key, value in s_dict.items():
    s_dict2[value].append(key)
for i in s_dict2:
    for i2 in sorted(s_dict2[i]):
        print(i2)