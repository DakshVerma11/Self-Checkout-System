import csv
import mysql.connector as con
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

shoppinglist = []
mycon = con.connect(host='localhost', user='root', passwd='welcome', database='customer')
cur = mycon.cursor()

def addproducts():
    with open('products.csv', 'a', newline="") as file:
        mywriter = csv.writer(file, delimiter=',')
        bar = input("Barcode: ")
        name = input("Name: ")
        cost = input("Cost: ")
        mywriter.writerow([bar, name, cost])

def update():
    bar = input("Barcode: ")
    with open('products.csv', 'r') as f1:
        list = []
        new = []
        r_obj = csv.reader(f1)
        for row in r_obj:
            if row[0] != bar:
                list.append(row)
            else:
                print('Record found')
                print(row)
                newcost = input("New cost: ")
                row[2] = newcost
                print(row)
                new.append(row)
                list.append(row)
        if len(new) == 0:
            print('The barcode does not exist')
        print(list)
    with open('products.csv', 'w', newline='') as f1:
        r_obj = csv.writer(f1)
        r_obj.writerows(list)

def delete():
    bar = input("Barcode: ")
    with open('products.csv', 'r') as f1:
        list = []
        new = []
        r_obj = csv.reader(f1)
        for row in r_obj:
            if row[0] != bar:
                list.append(row)
            else:
                print('Record found,', row, ' now deleting')
                new.append(row)
        if len(new) == 0:
            print('The barcode does not exist')
        print(list)
    with open('products.csv', 'w', newline='') as f1:
        r_obj = csv.writer(f1)
        r_obj.writerows(list)

def find(x):
    with open('products.csv', 'r', newline="") as f1:
        r_obj = csv.reader(f1, delimiter=",")
        count = 0
        for row in r_obj:
            if int(row[0]) == x:
                shoppinglist.append(row)
                count += 1
        if count == 0:
            print('Product not found')

def add():
    id = int(input('Enter Customer ID: '))
    name = input('Enter Name: ')
    name = "'" + name + "'"
    password = input('Enter password: ')
    password = "'" + password + "'"
    command = ('Insert into customer values (%s,%s,%s);' % (id, name, password))
    cur.execute(command)
    mycon.commit()

def select():
    name = input('Enter Name: ')
    password = input('Enter password: ')
    command = ("Select * from customer where name = '" + name + "'")
    cur.execute(command)
    result = cur.fetchone()
    if result and password == result[2]:
        print('Access granted, Welcome')
        return result
    else:
        print('Wrong password')

print('Welcome to self checkout')
print('''Are you a :
1 - New customer
2 - Returning Customer''')

ans = int(input('Answer: '))
if ans == 1:
    add()

customer = select()

while True:
    x = int(input('Enter Product Code: '))
    find(x)
    n = input('Do you want to add more items (y/n): ')
    if n != 'y':
        break

print('Final List is:')
print(*shoppinglist, sep='\n')

an = input('Continue (y/n)? ')
if an != 'y':
    exit()

now = datetime.now()
print('Generating Bill')
print('*' * 35)
print(now)
print(*customer, sep='\t')
total = 0
idlis = []
for i in shoppinglist:
    total += int(i[2])
    idlis.append(i[0])
    print(*i, sep='\t')

print('Total cost:', total)

payment = input('Enter Payment method (Cash/Card/UPI): ')

print('Thank you for shopping')
print('*' * 35)

# Generate PDF Bill
pdf_file_name = f'bill_{now.strftime("%H_%M_%S__%d_%m_%Y")}.pdf'  # Using current time and date in the file name
c = canvas.Canvas(pdf_file_name, pagesize=letter)
c.drawString(100, 750, 'Bill')
c.drawString(100, 730, f'Date: {now}')
c.drawString(100, 710, f'Customer ID: {customer[0]}')
c.drawString(100, 690, 'Shopping List:')
y = 670
for item in shoppinglist:
    c.drawString(120, y, f'Barcode: {item[0]}, Name: {item[1]}, Cost: {item[2]}')
    y -= 20
c.drawString(100, y, f'Total Cost: {total}')
c.drawString(100, y-20, f'Payment Method: {payment}')
c.drawString(100, y-40, 'Thank you for shopping!')
c.save()

print(f'PDF Bill saved as {pdf_file_name}')
