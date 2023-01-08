import mysql.connector as a

from prettytable import PrettyTable as pt

con=a.connect(host='localhost', user='root', passwd='1234',database='library_app')

def addbook():
    bn=input("Enter the Book Name: ")
    ba=input("Enter its Author's Name: ")
    c=int(input("Enter the ISBN Code: "))
    t=int(input("No. of  copies available : "))
    s=input("Enter its Genre: ")
    data=(bn,ba,c,t,s)
    sql='insert into books values(%s, %s,%s,%s,%s);'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("\nBook Added Successfully\n")
    wait = input("\nPress enter to continue..... \n")
    librarian()

def isEmpty(co):
    a="select total from books where bcode=%s;"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    data=c.fetchall()
    if data[0][0]<=0:
        return True
    else:
        return False

    
def issueb():
    n=input("Enter Student's Name: ")
    r=int(input("Enter Roll No.: "))
    co=int(input("Enter ISBN Code: "))
    if bookup(co):
        print("\n\n BOOK doesn't exist in our library \n\n Here are the books available in our library ")
        dispbook()
    elif isEmpty(co):
        print("\n\n Currently the book is out of stock :( \n Wait untill someone returns")
        student()
    else:
        a="insert into issue values(%s,%s,%s,CURDATE());"
        data=(n,r,co)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print("\nBook issued successfully by: ",n)
        wait = input("\nPress enter to continue..... \n")
        bookup(co,-1)
        student()
        
def returnb():
    n=input("Enter Student's Name: ")
    r=int(input("Enter  Roll No.: "))
    co=int(input("Enter ISBN Code: "))
   
    a="insert into retarn values(%s,%s,%s,CURDATE());"
    data=(n,r,co)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book returned by: ",n)
    wait = input("\nPress enter to continue..... \n")
    bookup(co, 1)
    student()

def bookup(co,u=0):
    a="select total from books where bcode=%s;"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    if myresult== None:
        return True
    else:
        t=myresult[0]+u
        sql="update books set total=%s where bcode=%s;"
        d=(t,co)
        c.execute(sql,d)
        con.commit()
        return False

def dbook():
    ac=int(input("Enter the ISBN Code: "))
    c=con.cursor()
    a="delete from books where bcode=%s;"
    data=(ac,)
    c.execute(a,data)
    con.commit()
    print("Book deleted successfully")
    wait = input("\nPress enter to continue.....\n")
    librarian()

def dispbook():
    c=con.cursor()
    a="select * from books;"
    c.execute(a)
    myresult=c.fetchall()
    if myresult == []:
        print("Sorry , No books available in our library")
    else:
        for i in myresult:
            print("Book name: ",i[0])
            print("Author: ",i[1])
            print("ISBN code: ",i[2])
            print("Total copies:",i[3])
            print("Genre:",i[4])
        wait = input("\nPress enter to continue.....\n")
        student()

def report_issued_books():
    c=con.cursor()
    a="select * from issue;"
    c.execute(a)
    data=c.fetchall()
    t=pt()
    t.field_names=['NAME','ROLL','ISBN NO.',' DATE']
    for i in data:
        t.add_row(list(i))
    t.align['NAME','ROLL','ISBN NO.',' ISSUE DATE']='c'
    print(t)
    wait = input("\nPress enter to continue.....\n")
    librarian()

def report_return_books():
    a="select * from retarn;"
    c=con.cursor()
    c.execute(a)
    data=c.fetchall()
    t=pt()
    t.field_names=['NAME','ROLL','ISBN NO.','RETURN DATE']
    for i in data:
        t.add_row(list(i))
    t.align['NAME','ROLL','ISBN NO.',' RETURN DATE']='c'
    print(t)
    wait = input("\nPress enter to continue.....\n")
    librarian()


def student():
     print("""
          [1] DISPLAY BOOK CATALOGUE  
          [2] ISSUE A BOOK
          [3] RETURN A BOOK
          [4] RETURN TO PREVIOUS MENU
          [0] EXIT PROGRAM
          
          """)
     choice=input("Enter Task No :")

     if(choice=='1'):
          dispbook()
     elif(choice=='2'):
        issueb()
     elif(choice=='3'):
        returnb()
     elif(choice=='0'):
        print("\n\nThank you and have a great day ahead................\n\n")
     elif(choice=='4'):
        main()
     else:
        print("Please try again........\n\n")
        student()

def librarian():
    print("""
          [1] ADD NEW BOOKS  
          [2] BOOK ISSUED HISTORY
          [3] BOOK RETURNED HISTORY
          [4] DELETE NON-ESSENTIAL BOOKS
          [5] RETURN TO PREVIOUS MENU
          [0] EXIT PROGRAM
          
          """)
    choice=input("Enter Task No :")

    if(choice=='1'):
          addbook()
    elif(choice=='2'):
        report_issued_books()
    elif(choice=='3'):
        report_return_books()
    elif(choice=='4'):
        dbook()
    elif(choice=='0'):
        print("\n\nThank you and have a great day ahead................\n\n")
    elif(choice=='5'):
        main()
    else:
        print("Please try again........\n\n")
        librarian()
def main():
    print("\t\t\t LIBRO - A LIBRARY MANAGEMENT APPLICATION\t\t\t")
    print("\t\t\t","-"*51)
    print("\t\t\t\t\t\t by Sagnik Sahoo\t\t\n\n")
    print("\n PRESS 0 to EXIT THE APP ")
    ch=input("Are you Student [1] or Libranian[2] ?")
    if ch=='1':
        student()
    elif ch=='2':
        librarian()
    else:
        print("Please try again........\n")
        main()
        

  
main()

