#  5) Poetry (non-recursable)

def Next(a, N):
    global t
    i = N - 2
    while (i >= 0) and (a[i] >= a[i+1]):
        i -= 1
    if i < 0:
        t = False
        return t
    else:
        j = N - 1
        while (j > 0) and (a[j] <= a[i]):
            j -= 1

        a[i], a[j] = a[j], a[i]

        for i2 in range (i + 1, N):
            for j2 in range(i2 + 1, N):
                if a[i2] >= a[j2]:
                    a[i2], a[j2] = a[j2], a[i2]    


N = int(input())
nums = list(map(int, input().split()))
if len(nums) != N:
    print('Enter ' + N + ' values!')
    quit()

# processing list of entered nums to the pattern: "01010101..."
pattern = ''
cur_bool = '0'
nums_pr = []
for ic in range(N):
    processed = ''
    for jc in range(1, nums[ic]+1):
        processed += cur_bool;
        pattern += cur_bool;  # forming pattern
        if cur_bool == '0': cur_bool = '1'
        else: cur_bool = '0'
    nums_pr.append(processed)

# checking all possible permutations
a = []
perm_count = 0
for ic in range(N):
    a.append(ic)
t = True
while t:
    permutation =''
    for ic in range(N):
        permutation += nums_pr[a[ic]]
    if permutation == pattern:
        perm_count += 1
        print(permutation + '  - OK')
    else:
        print(permutation + '  - not ok')
    Next(a, N)
print('\n\nNumber of possible permutations: ' + str(perm_count))
    
    
