def largestNum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

def main():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    num3 = float(input("Third number: "))

    print(largestNum(num1,num2,num3))

main()