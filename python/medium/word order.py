occurence = dict()
wordList = []
n = int(input())
for _ in range(n):
    word = input()
    if word in occurence:
        occurence[word] = occurence[word] + 1
    else:
        occurence[word] = 1
        wordList.append(word)
print(len(wordList))
result = ""
for word in wordList:
    result = result + str(occurence[word]) + " "
print(result)
