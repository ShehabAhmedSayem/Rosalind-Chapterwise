# Problem Name: Implement PatternToNumber


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
       
    return string


word_to_num = {'A':0, 'C':1, 'G':2, 'T':3}

def patternToNumber(pattern):
    
    if not pattern:
        return 0
    
    return 4 * patternToNumber(pattern[:-1]) + word_to_num[pattern[-1]]    
    


if __name__ == "__main__":
    pattern = read_input_from_file("in.txt")
   
    patternToNumber(pattern)
    
    