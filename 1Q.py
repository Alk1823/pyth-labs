
dic = {}
contin = "yes"
while contin.lower() == "yes".lower():
    emp = input("Enter Employee name: ")
    sal = input("Enter salary: ")
    dic[emp] = sal
    contin = input("Do you want to continue? ")



print(dic)