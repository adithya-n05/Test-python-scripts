dicS = {}
dicT = {}

s="Qatar"
t ="kalita"

for i in s:
            print(i)
            if i in dicS:
                dicS[i] = dicS[i] + 1
            else:
                dicS[i] = 1
        
for i in t:
            if i in dicT:
                dicT[i] = dicT[i] + 1
            else:
                dicT[i] = 1

for i in t:
            if i not in dicS:
                   print(False)
            elif dicS[i] != dicT[i]:
                   print(False)
            else:
                   print(True)