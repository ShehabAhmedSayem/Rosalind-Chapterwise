'''
Problem Name: Find a Position in a Genome Minimizing the Skew
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
       
    return string


def min_skew(dna):
    min_pos = []
    min_value = len(dna)+1
    count = 0
    for i in dna:
        if i == 'C':
            count-=1
        elif i == 'G':
            count+=1
        if count < min_value:
            min_value = count
        min_pos.append(count)
        
    return min_pos, min_value

    

if __name__ == "__main__":
    dna_string = read_input_from_file("in.txt")
    
    min_pos, min_value = min_skew(dna_string)
    ans = ''
    for i in range(len(dna_string)):
        if min_pos[i] == min_value:
            ans += (str(i+1)+' ')
    print(ans)
    