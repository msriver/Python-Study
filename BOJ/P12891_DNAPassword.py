import sys
input = sys.stdin.readline

s, p = map(int, input().rstrip().split())
dna_str = input().rstrip()

nums = [int(x) for x in input().rstrip().split()]
criteria = {'A': nums[0], 'C': nums[1], 'G': nums[2], 'T': nums[3]}

def is_valid_dna_str(str_count_map, criteria):
    dna_char_set = {'A', 'C', 'G', 'T'}
    for dna_chr in dna_char_set:
        if str_count_map[dna_chr] < criteria[dna_chr]:
            return False
    return True

window = dna_str[:p]
window_map = {
    'A': window.count('A'),
    'C': window.count('C'),
    'G': window.count('G'),
    'T': window.count('T')
}
count = 0

if is_valid_dna_str(window_map, criteria):
    count += 1

for i in range(p, s):
    window_map[dna_str[i]] += 1
    window_map[dna_str[i - p]] -= 1
    if is_valid_dna_str(window_map, criteria):
        count += 1

print(count)