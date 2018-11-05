# Problem Name: Implement NumberToPattern


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        number = file.readline().strip()
        k = file.readline().strip()
    return number, k


num_to_word = {0:'A', 1:'C', 2:'G', 3:'T'}

def numberToPattern(index, k):
    
    if k == 1:
        return num_to_word[index]
    
    prev_index = index // 4
    r = index % 4
    
    return numberToPattern(prev_index, k-1) + num_to_word[r]  
    

if __name__ == "__main__":
    number, k = read_input_from_file("in.txt")

    print(numberToPattern(number, k))
    