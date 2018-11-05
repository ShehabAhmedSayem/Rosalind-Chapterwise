'''
Problem Name: Compute the Hamming Distance Between Two Strings
'''

def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        string1 = file.readline().strip()
        string2 = file.readline().strip()
       
    return string1, string2


def hammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance+=1
    return distance

    

if __name__ == "__main__":
    s1, s2 = read_input_from_file("in.txt")
    
    distance = hammingDistance(s1,s2)    

    print(distance)