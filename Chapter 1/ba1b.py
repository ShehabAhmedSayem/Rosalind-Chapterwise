# Problem Name: Find the Most Frequent Words in a String


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        k = int(file.readline().strip())
       
    return string, k

def most_frequent_kmer(string, k):
    '''
    string: input string
    k: length of kmers
    '''
    
    pattern_occurences = dict()
    
    l = len(string)
    most_occurence = 0
    
    for i in range(l-k+1):
        pattern = string[i:i+k]
        
        if pattern in pattern_occurences.keys():
            pattern_occurences[pattern] += 1
        else:
            pattern_occurences[pattern] = 1
            
        if pattern_occurences[pattern] > most_occurence:
            most_occurence = pattern_occurences[pattern]
    
    return pattern_occurences, most_occurence

    
    

if __name__ == "__main__":
    string, k = read_input_from_file("in.txt")
    
    pattern_dict, most_occurence = most_frequent_kmer(string, k)

    for k, v in pattern_dict.items():
        if v == most_occurence:
            print(k)
    
    