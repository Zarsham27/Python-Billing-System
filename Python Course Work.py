# use of funtion is in four types Menu, Purchase, Discount& Receipt

def Menu():
    name=input('Please type your name')
    print('Welcome to Leather Tree London!',name,)
    print('Product Availble on our Website are as Follows')
    print('-----------------------------------------------')
    print('1. Wallet \t £20')
    print('2. Belts \t £10')
    print('3. Bags \t £50')
    print('4. Shoes \t £90')
    print('5. Jackets \t £40')
    print('6. Hand Bags \t £50')
    print('7. Phone Case \t £20')
    print('-----------------------------------------------')
    Purchase(name)
    

def Purchase(name):

# use of Loop (while) and List has been shown in this section

    Table=[] 
    sumtotal=0
    Product=input('Please enter the product name you want to purchase ')
    Table.append(Product)
    print('Your Basket',Table)
    Price=int(input('Please enter the price '))
    Quantity=int(input('Enter quantity '))
    print('Amount £',Price*Quantity)
    total=Price*Quantity
    sumtotal=sumtotal+total
    another=input('Do you want to add another product? ')
    while another.lower()=='yes':
        Product=input('Please enter the additional products name you want to buy ')
        Table.append(Product)
        print('Your Basket',Table)
        Price=int(input('Please enter the price '))
        Quantity=int(input('Enter quantity '))
        print('Amount £',Price*Quantity)
        total=Price*Quantity
        sumtotal=sumtotal+total
        another=input('Do you want add another product? ')
        print('Your Basket',Table)

    print('Total £',sumtotal)

    Returning='yes'
    Return=input('Do you want to remove any product from your basket ')
    if Return.lower()==Returning:
        Product=input('Please enter the product name ')
        Price=int(input('Please enter price '))
        Quantity=int(input('Please enter quantity '))
        Table.remove(Product)
        print('Your Basket',Table)
        returntotal=Price*Quantity
        finaltotal=sumtotal-returntotal
        Return=input('Do you want to remove anything else? ')
        print('Total Amount £',finaltotal)
    
    print('-----------------------------------------------')
    Discount(Product,Quantity,name,sumtotal,Table,finaltotal)
    

def Discount(Product,Quantity,name,sumtotal,Table,finaltotal):

# use of Boolean and Branching (Nesting) has been shown in this section

    Student_Discount= 'yes'
    Promotion_Discount= 'no'
    
    print('Please Select a Following Option \n')
    print('Yes for Student Discount \n')
    print('No for Promotion Discount \n')
    print('Coupon Discount please enter any word and then yes \n')
    print('For No Discount please enter any word and then no \n')
    
    Discount=input('Please Enter Here = ')
        
    if Discount.lower()== Student_Discount:
          print('Student Discount 25%',finaltotal/100*25)
          Grandtotal=finaltotal-finaltotal/100*25
          print('£',Grandtotal)
          
    elif Discount.lower()==Promotion_Discount:
          print('Promotion Discount 15%',finaltotal/100*15)
          Grandtotal=finaltotal-finaltotal/100*15
          print('£',Grandtotal)
          
    else :
        Coupon_Discount=input('Do you have a Coupon ')
        if Coupon_Discount.lower()=='yes':
            print('Coupon Discount 20%',finaltotal/100*20)
            Grandtotal=finaltotal-finaltotal/100*20
            print('£',Grandtotal)
            
        else :
                print('No Discount')

                Grandtotal=finaltotal
     
    print('-----------------------------------------------')
    Receipt(Product,Quantity,name,Grandtotal,Table)


def Receipt(Product,Quantity,name,Grandtotal,Table):

# use of for loop and list is been shown in this section

    import datetime
    x=datetime.datetime.now()
    
    print('-----------------------------------------------')
    print('Receipt \n')
    print('Leather Tree \n')
    print('Order Number','123456789 \n')
    print(name)
    print(x)
    
    for y in Table:
        print (y,'x',Quantity)
        
    print('Total Amount £',Grandtotal,' \n')
    print('Tracking Number','123456789 \n')
    print('Thank You,',name,'for shopping at Leather Tree')
    print('-----------------------------------------------')
    
Menu()




