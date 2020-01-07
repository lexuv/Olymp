#  5) Poetry (recursable)

def generate(n, prefix):
    global perm_count, permutation
    if len(prefix) == n:
        permutation =''
        for ic in range(N):
            permutation += nums_pr[prefix[ic]-1]
        if permutation == pattern:
            perm_count += 1
            print(prefix, permutation + '  - OK')
        else:
            print(prefix, permutation + '  - not ok')        
    else:
        for next in range(1, n + 1):
            if next not in prefix:
                generate(n, prefix + [next])


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
prefix = []
perm_count = 0
    
generate(N, prefix)    
    
print('\n\nNumber of possible permutations: ' + str(perm_count))