def boardCutting(cost_y, cost_x):
    
    # order horizontal + vertical slices
    
    cost = [[x,"x"] for x in cost_x]
    for y in cost_y:
        cost.append([y,"y"])
    cost = sorted(cost, key= lambda l : l[0],reverse = True)
    total, x_cuts, y_cuts = 0,1,1
    for [x,t] in cost:
        
        if t == "x":
            total += y_cuts * x
            x_cuts += 1
        else:
            total += x_cuts * x
            y_cuts += 1

    return total%(10**9 + 7)   
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()
