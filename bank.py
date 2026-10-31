
#Program for a mini ATM which work on pin and account number

import mysql.connector 
mydb=mysql.connector.connect(user="root",host="localhost",password="arun8090",database="banking",port=3306)
cur=mydb.cursor()
opt='y'
while opt=='y':
    print("\n\n")
    acc=int(input("Enter your account no: "))
    pin=int(input("Enter your pin: "))
    print('''\n\nWelcome to your Bank ATM\n\nChoose the operation:\n\n1. Balance Enquiry    \t2. Withdrawl
\n3. PIN Change         \t4. Last Transaction detail
          \n5.Edit Credentials     \t6.Loaning\n''')
    ch=int(input("Enter choice: "))

    tp=(acc,pin)
    if ch==1:
        cur.execute("select balance from customer where acount_no=%s and pin=%s",tp)
        t=cur.fetchone()
        cur.execute("select name from customer where acount_no=%s and pin=%s",tp)
        nm=cur.fetchone()
        print("The balance in account ",acc,"of account holder",nm,"is",t)
        ex=input("\nPress any key to end the session: ")
        if ex==0:
            break
    elif ch==2:
        amnt=int(input("Enter the amount to be withdrawn: "))
        tp2=(amnt,acc,pin)
        cur.execute("update customer set balance=balance-%s where acount_no=%s and pin=%s",tp2)
        print("Transaction Successfull !!!")
        cur.execute("update customer set last_transaction=%s where acount_no=%s and pin=%s",tp2)
        ex=int(input("Press 1 to see available balance and 0 to exit: "))
        if ex==1:
            cur.execute("select balance from customer where acount_no=%s and pin=%s",tp)
            t=cur.fetchone()
            print("The balance in account ",acc,"is",t)
            
        else:
            print("session expired !!!\n\n")
    elif ch==3:
        pn=int(input("Enter a new pin of 4 digits: "))
        tp1=(pn,acc,pin)
        cur.execute("update customer set pin=%s where acount_no=%s and pin=%s",tp1)
        print("PIN changed successfully !!!")
        ex=input("Press 0 to end the session: ")
        if ex==0:
            break
    elif ch==4:
        cur.execute("select last_transaction from customer where acount_no=%s and pin=%s",tp)
        t=cur.fetchone()
        cur.execute("select name from customer where acount_no=%s and pin=%s",tp)
        nm=cur.fetchone()
        print("The last transaction in account=",acc,"of account holder",nm,"is",t)
        ex=input("Press 0 to end the session: ")
        if ex==0:
            break
    elif ch==5:
         print("\nChoose the operation:\n\n1. Edit name    \t2. Edit Mob No")
         ch1=int(input("Enter choice: "))
         if ch1==1:
             nm=input("Enter the correct name: ")
             tp5=(nm,acc)
             cur.execute("update customer set name=%s where acount_no=%s",tp5)
             print("Task accomplished \n")
             
             
         elif ch1==2:
            mb=int(input("Enter the updated mobile number: "))
            tp6=(mb,acc)
            cur.execute("update customer set name=%s where acount_no=%s",tp6)
            print("Task accomplished\n")
            

    elif ch==6:
        p=int(input("Enter the loan amount: "))
        n=int(input("Enter the period of years: "))
        n=n*12
        r=0.09/12
        emi=p*r*(((r+1)**n)/(((r+1)**n)-1))
        print("Your estimated EMI per month at rate of 9% is",emi)
        print("Choose operation:\n1.Take loan   \t2.Discard")
        ch3=int(input("Enter your choice: "))
        if ch3==1:
            tp4=(p,acc,pin)
            cur.execute("update customer set balance=balance+%s where acount_no=%s and pin=%s",tp4)
            cur.execute("update customer set last_transaction=%s where acount_no=%s and pin=%s",tp4)
            cur.execute("update customer set loan=%s where acount_no=%s and pin=%s",tp4)
            print("Amount Credited to   your account.......")
        else:
            print("Loan request Discarded !!!\n\n")
    else:
        print("Invalid Choice !!!")
        print("Invalid Choice !!!")
        print("Session expired")
        opt='y'
    opt='y'     
mydb.commit()
