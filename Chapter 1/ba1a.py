# Problem Name: Compute the Number of Times a Pattern Appears in a Text


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        pattern = file.readline().strip()
       
    return string, pattern

def occurrence(string, pattern):
    """
    string: input string
    pattern: pattern to search
    """
    
    count = 0
    l = len(string)
    p = len(pattern)
    
    for start in range(l-p+1):
        if(string[start:start+p] == pattern):
            count += 1
    
    return count

    
    

if __name__ == "__main__":
    string, pattern = read_input_from_file("in.txt")
    print(occurrence(string, pattern))