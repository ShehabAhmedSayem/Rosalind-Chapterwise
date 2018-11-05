'''
Problem Name: Find All Approximate Occurrences of a Pattern in a String
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        pattern = file.readline().strip()
        dna = file.readline().strip()
        distance = file.readline().strip()
        
    return pattern, dna, distance


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

    

if __name__ == "__main__":
    pattern, dna, distance = read_input_from_file("in.txt")
    
    pattern_list = approximatePattern(pattern, dna, distance)
    answer = ''
    for i in pattern_list:
        answer += (str(i) + ' ')
    print(answer)
    
    