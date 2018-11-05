# Problem Name: Generate the d-Neighborhood of a String


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        d = file.readline().strip()
    return string, int(d)


def hammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance+=1
    return distance

def dNeighbours(string, distance):
    string = list(string)
    string_length = len(string)
    output = []
    
    x = ['C', 'T', 'G', 'A']
    pattern_dict = {''.join(p): 0 for p in itertools.product(x, repeat=string_length)}
    
    for p in pattern_dict.keys():
        if hammingDistance(string, p) <= distance:
            output.append(p)
    return output


if __name__ == "__main__":
    string, d = read_input_from_file("in.txt")

    dNeighbour_list = dNeighbours(string,d)    

    ans = ''
    for i in dNeighbour_list:
        ans += (i+'\n')
    print(ans)

    