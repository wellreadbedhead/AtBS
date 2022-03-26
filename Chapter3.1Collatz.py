def collatz(a):
    if a%2 == 0:
        a //= 2
        print(str(a))
        return(a)
    elif a%2 == 1:
        a = a * 3 + 1
        print(str(a))
        return(a)
    else:
        print("Please only enter integers")

def getToOne():
    try:
        a = int(input("Enter an integer: "))
        while a != 1:
            a = collatz(a)
    except ValueError:
        print("Please only enter integers")

getToOne()