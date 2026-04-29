
def findGCD(num1,num2):
    a,b= (num1,num2) if num1>num2 else (num2,num1)

    while b!=0:
        Q=a//b
        rem=a%b
        a,b=b,rem

    return a


if __name__=="__main__":
    print(findGCD(6,12))

