# Problem Name: Find All Occurrences of a Pattern in a String


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        pattern = file.readline().strip()
        string = file.readline().strip()
       
    return string, pattern


def all_occurence_of_pattern(string, pattern):
    """
    string: input string
    pattern: pattern to find all occurences
    """
    index_list = []
    l = len(string)
    p = len(pattern)
    
    for start in range(l-p+1):
        if(string[start:start+p] == pattern):
            index_list.append(start)
    
    return index_list
    
    

if __name__ == "__main__":
    string, pattern = read_input_from_file("in.txt")
    
    index_list = all_occurence_of_pattern(string, pattern)
    answer = ''
    for i in index_list:
        answer += (str(i) + ' ')
    print(answer)
    
    