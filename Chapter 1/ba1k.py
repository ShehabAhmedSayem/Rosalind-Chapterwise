'''
Problem Name: Generate the Frequency Array of a String
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        k = file.readline().strip()
       
    return string, int(k)


def frequencyArray(dna, k):
    x = ['A', 'C', 'G', 'T']
    pattern_dict = {''.join(p): 0 for p in itertools.product(x, repeat=k)}
   
    for i in range(len(dna) - k + 1):
        p = dna[i: i+k]
        pattern_dict[p] += 1
    return pattern_dict


if __name__ == "__main__":
    dna, k = read_input_from_file("in.txt")
    
    ans = ''
    f_arr = frequencyArray(dna,k)
    for p in f_arr.keys():
        ans += (str(f_arr[p]) + ' ')
    print(ans)
    