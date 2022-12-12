import os

def hackerrankInString(s):
    ref = "hackerrank"
    j = 0
    for i in range(len(s)):
        j += s[i] == ref[j]
        if j>=len(ref): return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
