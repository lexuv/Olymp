#  3) Music

enter = list(map(int, input().split()))
n = enter[0]
k = enter[1]
tries = 1
current = 1
while current != k:
    tries += 1
    current += 6
    if current > n:
        current -= n
        if current == 1:
            tries = 0
            break
print (tries)
    
    

        