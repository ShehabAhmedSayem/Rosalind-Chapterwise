'''
Problem Name: Find Patterns Forming Clumps in a String

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome
if there is an interval of Genome of length L in which Pattern appears at least t times.
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        k, L, t = file.readline().strip().split()
       
    return string, int(k), int(L), int(t)


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


def find_clumps(string, k, L, t):
    clump_list = []

    for start in range((len(string) - L + 1)):
        temp_str = string[start: start + L]
        
        for start_temp in range((L - k + 1)):
            pattern = temp_str[start_temp: start_temp + k]
            if occurrence(temp_str, pattern) >= t and pattern not in clump_list:
                clump_list.append(pattern)

    return clump_list

    

if __name__ == "__main__":
    string, k, L, t = read_input_from_file("in.txt")
    
    clump_list = find_clumps(string, k, L, t)
    answer = ''
    for i in clump_list:
        answer += (str(i) + ' ')
    print(answer)
    
    