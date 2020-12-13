import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Nano1234",database="project")
mycursor=mydb.cursor()
print(" If you are a new student and want to register press 1")
print(" if you want to borrow a book press 2")
print(" If you want to return the book press 3")
choice=int(input(" Enter your choice"))
if choice ==1:
    query ="INSERT INTO comp(ID, Name, Class) VALUES (%s, %s, %s)"
    import random
    n = random.randint(1000,9999)
    a=input("Enter your name")
    b=input("Enter your class")
    r=(n,a,b)
    mycursor.execute(query,r)
    print("Your new library ID is",n)
if choice == 2:
    s="Select * from comp where ID=%s"
    i=int(input(" enter your ID"))
    r=(i,)
    mycursor.execute(s,r)
    for x in mycursor:
        print(x)
    mycursor=mydb.cursor()
    sql = "update comp set book=%s where ID=%s"
    val = input("Enter the name of book")
    r=(val,i)
    mycursor.execute(sql, r)
    query="update comp set date=%s where ID=%s"
    import time    
    a = time.strftime('%Y-%m-%d')
    p=(a,i)
    mycursor.execute(query, p)
    print("Now you have 7 days to return your book otherwise you will be fined")

if choice == 3:
    a="SELECT DATEDIFF(CURDATE(), 'select date from comp where ID=%s')"
    i=int(input(" enter your ID"))
    r=(i,)
    mycursor.execute(a,r)
    for x in mycursor:
        if x == (None,):
            q="update comp set Book=Null where ID=%s"
            s="update comp set Date=Null where ID=%s"
            a=(i,)
            b=(i,)
            mycursor.execute(q,a)
            mycursor.execute(s,b)
            print("Your record has been deleted") 
        if x != (None,):
            q="update comp set Book=Null where ID=%s"
            s="update comp set Date=Null where ID=%s"
            a=(i,)
            b=(i,)
            mycursor.execute(q,a)
            mycursor.execute(s,b)
            print("Your record has been deleted")
            if x>7:
                q="update comp set Book=Null where ID=%s"
                s="update comp set Date=Null where ID=%s"
                a=(i,)
                b=(i,)
                mycursor.execute(q,a)
                mycursor.execute(s,b)
                print("You will have to pay 100 rupee fine to your librarian for not returning your book on time")
                

else:
    print("good")
mydb.commit()

