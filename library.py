import mysql.connector as a 
con=a.connect(host='localhost', user='root', passwd='root',database='library_app')

def addbook():
    bn=input("Enter Book Name: ")
    ba=input("Enter Author's Name: ")
    c=int(input("Enter Book Code: "))
    t=int(input("Total Books: "))
    s=input("Enter Subject: ")
    data=(bn,ba,c,t,s)
    sql='insert into books values(%s, %s,%s,%s,%s);'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("\ \n n\nBook Added Successfully.......... \n\n\n\n")
    wait = input("\n\n\nPress enter to continue..... \n\n\n\n\n\n")
    main()
                 
def issueb():
    n=input("Enter Student Name: ")
    r=int(input("Enter Reg No.: "))
    co=int(input("Enter Book Code: "))
    d=input("Enter Date: ")
    a="insert into issue values(%s,%s,%s,%s);"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("\\\\nBook issued successfully to: ",n)
    wait = input("\\n\nPress enter to continue..... (n\n\n\n\n\n")
    bookup(co,-1)
    main()

def returnb():
    n=input("Enter Student Name: ")
    r=int(input("Enter Reg No.: "))
    co=int(input("Enter Book Code: "))
    d=input("Enter Date: ")
    a="insert into return_ values(%s,%s,%s,%s);"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book returned by: ",n)
    wait = input("\\n\nPress enter to continue..... \n\n\n\n\n\n")
    bookup(co, 1)
    main()

def bookup(co,u):
    a="select total from books where bcode=%s;"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t-myresult[0]+u
    sql="update books set total=%s where bcode=%s;"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n")
    main()

def dbook():
    ac=int(input("Enter Book Code: "))
    c=con.cursor()
    a="delete from books where bcode=%s;"
    data=(ac,)
    c.execute(a,data)
    con.commit()
    print("Book deleted successfully")
    wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n\n\n\n\n\n\n")
    main()

def dispbook():
    c=con.cursor()
    a="select * from books;"
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book name: ",i[0])
        print("\n\n")
        print("Author: ",i[1])
        print("Book code: ",i[2])
        print("Total:",i[3])
        print("Subject:",i[4])
    wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n\n\n\n\n\n\n")
    main()

def report_issued_books():
    c=con.cursor()
    a="select * from issue;"
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print(myresult)
    wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n\n\n")
    main()

def report_return_books():
    a="select * from return_;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print(myresult)
    wait = input("\n\n\nPress enter to continue.....\n\n\n\n\n\n\n\n\n\n\n\n")
    main()

def main():
    print("""
                LIBRARY MANAGEMENT APPLICATION
        ________________________________________________________
          1. ADD BOOK
          2. ISSUE OF BOOK
          3. RETURN OF BOOK
          4. DELETE BOOK
          5. DISPLAY BOOKS
          6. REPORT MENU
          7. EXIT PROGRAM
          """)
    choice=input("Enter Task No:......")
    print("\n\n\n\n\n\n\n")
    if(choice=='1'):
          addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        returnb()
    elif(choice=='4'):
        dbook()
    elif(choice=='5'):
        dispbook()
    elif(choice=='6'):
        print(""" REPORT MENU
                ________________________
                1. ISSUED BOOKS
                2. RETURNED BOOKS
                3. GO BACK TO MAIN MENU
                \n\n\n
                """)
        choice=input("Enter Task No:......")
        print("\n\n\n\n\n\n\n")
        if choice=='1':
            report_issued_books()
        elif choice=='2':
            report_return_books()
        elif choice=='3':
            main()
        else:
            print("Please try again........\n\n\n\n\n\n\n\n\n")
            main()
    elif(choice=='7'):
        print("\n\n\n\n\n\n\n\n\n\n\n\nThank you and have a great day ahead................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print("Please try again........\n\n\n\n\n\n\n\n\n\n\n\n")
        main()
main()

