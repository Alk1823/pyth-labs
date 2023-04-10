def is_vowel(c):
    for i in c:
        if i.lower() == "a":
            return True
        if i.lower() == "e":
            return True
        if i.lower() == "i":
            return True
        if i.lower() == "o":
            return True
        if i.lower() == "u":
            return True
    return False

def main():
    s = input("Write any string: ")
    
    counter = 0
    for i in s:
        if is_vowel(i) == True:
            counter = counter + 1
    
    print("Vowel number is: "+str(counter))

main()


