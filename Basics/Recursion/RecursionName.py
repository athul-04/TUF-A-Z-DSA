
def printName(name,n):
    if n==0:
        return
    print(name,end="\n")
    printName(name,n-1)



printName("Athul",3)