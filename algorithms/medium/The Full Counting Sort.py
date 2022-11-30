def countSort(arr):
    sortArr = dict()
    indices = set()
    for k in range(len(arr)):
        arr[k][0] = int(arr[k][0])
        sortArr[arr[k][0]] = ""
        if k<len(arr)/2:
            arr[k][1] = "-"
        
    for [i,x] in arr:
        sortArr[i] = sortArr[i] + x + " "
        indices.add(i)
    
    indices = sorted(list(indices))
    result = ""
    for i in indices:
        result = result + sortArr[i]
        
    print(result)
    
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
