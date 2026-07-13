n = int(input())

# Code here

def printName(i,n):
    if i>n:
        return
    print("GFG",end=" ")
    printName(i+1,n)
    
printName(1,n)

    

