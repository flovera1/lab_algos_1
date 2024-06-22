m = int(input("m: "))
n = int(input("n: "))

def main():
    if m == 10:
        return m/n
    elif m == 5:
        return m*n
    elif m == 3:
        return m + n
    elif m == 2:
        #return m**n
        return pow(m, n)
    else:
        return m



print(main())
