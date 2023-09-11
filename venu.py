def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:  
     print("error")
    return a/b           

while True:
    print("calculator")
    print("perform operations:")
    print("1.add")
    print("2.substract")
    print("3.multiply")
    print("4.divide")
    print("5.quit")
    choice=input("enter choice:")
    if (choice=='5'):
        print("exist,goodbye")
    if choice in ['1','2','3','4']:
        n1=float(input("enter input1:"))
        n2=float(input("enter input2:"))
        if choice=='1':
            print("result:",add(n1,n2))
        elif choice=='2':
            print("result:",substract(n1,n2))
        elif choice=='3':
            print("result:",multiply(n1,n2))
        elif choice=='4':
            print("result:",divide(n1,n2))    
    else:
        print("invalid")   
