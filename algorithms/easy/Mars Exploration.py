import os

def marsExploration(s):
    ref = "SOS"
    j,result = 0,0
    for i in range(len(s)):
        result += s[i] != ref[j]
        j = (j+1)%3
    return result
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
