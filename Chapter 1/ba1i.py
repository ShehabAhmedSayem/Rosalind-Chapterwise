'''
Problem Name: Find the Most Frequent Words with Mismatches in a String
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        k, d = file.readline().strip().split()
       
    return string, int(k), int(d)


def approximatePattern(pattern, dna, distance):
    dna = list(dna)
    pattern = list(pattern)
    pattern_length = len(pattern)
    output = []
    
    for i in range(len(dna)-pattern_length):
        string1 = dna[i:i+pattern_length]
        if hammingDistance(string1, pattern) <= distance:
            output.append(i)
    return output

def frequentWordsWithMismatch(dna, k, d):
    x = ['G', 'A', 'C', 'T']
    pattern_dict = {p: 0 for p in itertools.product(x, repeat=k)}
    
    max_occur = 0

    for p in pattern_dict.keys():
        pattern_dict[p] = len(approximatePattern(p, dna, d))
        if pattern_dict[p] > max_occur:
            max_occur = pattern_dict[p]

    output = []
    for p in pattern_dict.keys():
        if pattern_dict[p] == max_occur:
            output.append(''.join(p))
    return output
    

if __name__ == "__main__":
    dna, k, distance = read_input_from_file("in.txt")
    
    pattern_list = frequentWordsWithMismatch(dna, k, distance)
    answer = ''
    for i in pattern_list:
        answer += (str(i) + ' ')
    print(answer)
    
    