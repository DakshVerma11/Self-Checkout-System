import csv

shoppinglist=[]

def addproducts():   
    with open('products.csv' , 'a',newline="" ) as file:
        mywriter = csv.writer(file,delimiter=',')
        bar=input("Barcode.:")       
        name=input("Name:")
        cost=input("Cost:")
        mywriter.writerow([bar,name,cost])
     

            

def update():
    list=[]
    bar=input("Barcode.:")
   
    f1=open('products.csv' , 'r')
    new=[]
   
    r_obj=csv.reader(f1)
    for row in r_obj:
        if row[0]!=bar:
            list.append(row)
        else:
            print('Record found')
            print(row)
            newcost=input("New cost:")
            row[2]=newcost
            print(row)
            new.append(row)
            list.append(row)
    if len(new)==0:
        print('The bar no doesn\'t exist')
    print(list)
    f1.close()
   
   
    f1=open('products.csv' , 'w',newline='')
    r_obj=csv.writer(f1)
    r_obj.writerows(list)
    
    
def delete():
    list=[]
    bar=input("bar No.:")
   
    f1=open('products.csv' , 'r')
    new=[]
   
    r_obj=csv.reader(f1)
    for row in r_obj:
        if row[0]!=bar:
            list.append(row)
        else:
            print('Record found,',row,' now deleting')
            new.append(row)
    if len(new)==0:
        print('The bar no doesn\'t exist')
    print(list)
    f1.close()
   
   
    f1=open('products.csv' , 'w',newline='')
    r_obj=csv.writer(f1)
    r_obj.writerows(list)
    
    

     
def find(x):
    with open('products.csv' , 'r',newline="" ) as f1:
        r_obj=csv.reader(f1,delimiter=",")
        count=0   
        for row in r_obj:
            if int(row[0])==x:
                shoppinglist.append(row)
                count+=1
            
        if count==0:
            print('Product not found')
            
            
            
'''SQL'''

import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='welcome',database='customer')
cur=mycon.cursor()

def add():
    id=int(input('Enter Customer ID'))
    name=input('Enter Name')
    name="'"+name+"'"
    password=(input('Enter password'))
    password="'"+password+"'"
    command=('Insert into customer values (%s,%s,%s);'%(id,name,password))
    cur.execute(command)
    mycon.commit()
    
def select():
    name=input('Enter Name :')
    password=input('Enter password :')
    command= ("Select * from customer where name = '"+name+"'")
    cur.execute(command)
    if password==cur[2]:
        print('Acess granted, Welcome')
        customer=cur
    else:
        print('Wrong password')
    return customer





print('Welcome to self checkout')
print('''Are you a :
1 - New customer
2 - Returning Customer''')
            
ans=int(input( 'Answer:'))
if ans==1:
    add()
    
customer=select()

n='y'
while n='y':
    x=int(input('Enter Product Code'))
    find(x)
    n=input('Do you want to add more items (y/n) :')
    
print('Final List is :')
print(*shoppinglist, sep='\n')

an=input('Continue (y/n)?')
if an='n':
    break

from datetime import datetime
now = datetime.now()

print('Generating Bill')

print('*'*35)
print(now)
print(*customer, sep='\t')
total=0
idlis=[]
for i in shoppinglist:
    total+=i[2]
    idlist.append(i[0])
    print(*i,sep='\t')
    

    
print('Total cost :',total)


payment=input('Enter Payment method: (Cash/Card/UPI): ')

print('Thank you for shopping')
print('*'*35)




with open('Billings.csv' , 'a',newline="" ) as file:
    mywriter = csv.writer(file,delimiter=',')
    id=customer[0]       
    mywriter.writerow([id,idlis,total,payment,now])
            