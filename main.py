zakres1 = []

for i in range(1,101):
  if i%5==0:
    zakres1.append(i)
print(zakres1)
zakres2 = [number * number * number for number in zakres1]
print(zakres2)
print(zakres2*zakres1)
    
