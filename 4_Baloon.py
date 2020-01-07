#  4) Baloon

enter = list(map(int, input().split()))
N = enter[0]
W = enter[1]
if len(enter) != 2:
    print("Enter 2 values!")
    quit()    
packs = list(map(int, input().split()))
if len(packs) != N:
    print("Enter " + str(N) + " packs!")
    quit()
packs_sorted = sorted(packs)
counter_packs = 0
counter_weight = 0
for i in packs_sorted:
    counter_weight += i
    if counter_weight < W:
        counter_packs += 1
print (counter_packs)

