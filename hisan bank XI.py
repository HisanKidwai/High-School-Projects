a=[9000000,10000,20000]
p=[1234,4321,0000]
print("**************************Welcome to our Bank**********************************")
pin=int(input("Enter your pin"))
if pin != p[0] and pin != p[1] and pin != p[2]:
    print("Sorry, the pin you entered is incorrect")
    print("Forgot Pin")
    print("Press Y to change your pin or N to exit")
    m=input("Please enter your choice")
    if m ==("N"):
        raise SystemExit(0)
    if m == ("Y"):
        m=int(input("Enter your registered phone number"))
        if pin != p[0] and m == (8707318997):
            o=int(input("Please enter your OTP"))
            if o == (9000):
                e=int(input("Please enter your new pin"))
                p.insert(0,e)
                print("Your password has been changed successfully")
        if pin != p[1] and m == (1234567890):
            o=int(input("Please enter your OTP"))
            if o == (8000):
                e=int(input("Please enter your new pin"))
                p.insert(1,e)
                print("Your password has been changed successfully")
        if pin != p[2] and m == (1234567899):
            o=int(input("Please enter your OTP"))
            if o == (7000):
                e=int(input("Please enter your new pin"))
                p.insert(2,e)
                print("Your password has been changed successfully")
pin=int(input("Enter your pin"))
if pin == p[0]:
    print("Hisan has logged in successfully")
if pin == p[1]:
    print("Welcome Aryan to our bank")
if pin == p[2]:
    print("Welcome Pari to our bank")
def main():
    print("Please Press 1 For Your Balance")
    print("Please Press 2 To Make a Withdrawl")
    print("Please Press 3 To Pay in")
    c=int(input("enter your choice"))
    if pin == p[0] and c == 1:
        print("The balance is",a[0])
        print("Press Y to continue or N to exit")
        v=input("Enter your choice")
        if v == ("N"):
            print("******************Hope that you have great day_________Thank you****************")
            raise SystemExit(0)
        if v == ("Y"):
            main()
    if pin == p[1] and c == 1:
        print("The balance is",a[1])
        print("Press Y to continue or N to exit")
        v=input("Enter your choice")
        if v == ("N"):
            print("******************Hope that you have great day_________Thank you****************")
            raise SystemExit(0)
        if v == ("Y"):
            main()
    if pin == p[2] and c == 1:
        print("The balance is",a[2])
        print("Press Y to continue or N to exit")
        v=input("Enter your choice")
        if v == ("N"):
            print("******************Hope that you have great day_________Thank you****************")
            raise SystemExit(0)
        if v == ("Y"):
            main()
    if pin == p[0] and c == 2:
        z=int(input("Enter your amount"))
        a[0]=a[0]-z
        if z>a[0]:
            print("Thats more than what you have in your account")
        else:
            print("Your new balance is",a[0])
            print("******************Hope that you have great day_________Thank you****************")
    if pin == p[1] and c == 2:
        z=int(input("Enter your amount"))
        a[1]=a[1]-z
        if z>a[1]:
            print("Thats more than what you have in your account")
        else:
            print("Your new balance is",a[1])
            print("******************Hope that you have great day_________Thank you****************")
    if pin == p[2] and c == 2:
        z=int(input("Enter your amount"))
        a[2]=a[2]-z
        if z>a[1]:
            print("Thats more than what you have in your account")
        else:
            print("Your new balance is",a[2])
            print("******************Hope that you have great day_________Thank you****************")
    if pin == p[0] and c == 3:
        d=int(input("Enter the amount to be deoposited"))
        a[0]=a[0]+d
        print("Your new balance is",a[0])
        print("******************Hope that you have great day_________Thank you****************")
    if pin == p[1] and c == 3:
        d=int(input("Enter the amount to be deoposited"))
        a[1]=a[1]+d
        print("Your new balance is",a[1])
        print("******************Hope that you have great day_________Thank you****************")
    if pin == p[2] and c == 3:
        d=int(input("Enter the balance to be deoposited"))
        a[2]=a[2]+d
        print("Your new balance is",a[2])
        print("******************Hope that you have great day_________Thank you****************")
main()

    
    

   



        
