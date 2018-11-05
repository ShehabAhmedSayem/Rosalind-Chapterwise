'''
Problem Name: Find Frequent Words with Mismatches and Reverse Complements
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        k, d = file.readline().strip().split()
       
    return string, int(k), int(d)


def reverse_complement(string):
    rev_str = string[::-1]
    complement_rev = ''
    
    for i in range(len(string)):
        if(rev_str[i]=='A'):
            complement_rev += 'T'
        elif(rev_str[i]=='T'):
            complement_rev += 'A'
        elif(rev_str[i]=='C'):
            complement_rev += 'G'
        elif(rev_str[i]=='G'):
            complement_rev += 'C'
    
    return complement_rev

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

def frequentWordsWithMismatchAndRevComplement(dna, k, d):
    x = ['A', 'T', 'G', 'C']
    pattern_dict = {p: 0 for p in itertools.product(x, repeat=k)}
    
    max_occur = 0

    for p in pattern_dict.keys():
        pattern_dict[p] = len(approximatePattern(p, dna, d))
        pattern_dict[p] += len(approximatePattern(reverse_complement(p), dna, d))
        if pattern_dict[p] > max_occur:
            max_occur = pattern_dict[p]

    output = []
    for p in pattern_dict.keys():
        if pattern_dict[p] == max_occur:
            output.append(''.join(p))
    return output
    

if __name__ == "__main__":
    dna, k, distance = read_input_from_file("in.txt")
    
    pattern_list = frequentWordsWithMismatchAndRevComplement(dna, k, distance)
    answer = ''
    for i in pattern_list:
        answer += (str(i) + ' ')
    print(answer)
    
    