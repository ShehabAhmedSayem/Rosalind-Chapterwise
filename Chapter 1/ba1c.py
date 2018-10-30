# Problem Name: Find the Reverse Complement of a String


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
       
    return string


def reverse_complement(string):
    """
    string: string to reverse and complement
    """
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
    
    

if __name__ == "__main__":
    string = read_input_from_file("in.txt")
    
    print(reverse_complement(string))
    
    