print ('welcome to the Azubi Shop Portal')
print ()
print ('Here are the Statistics for last week...')
print ()

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#finding price average using a for loop
av_price =0
for price in prices:
    av_price += price

av_price/= len(prices )


print ("The total price average for all products = ${} ".format(av_price))
print ()


#updating price list
new_price=[]
for price in prices:
    new_price.append(price-5)

print ('the new price list is as follows :')
for item in products:
    i=0
    print ('{} = ${}'.format(item,new_price[i]))
    i+= 1
    
        
print ()

#finding total revenue of products 
for price in prices:
    for item in last_week:
        rev = 0
        rev+=(price * item)
print ('Total revenue of products is = ${}'.format(rev))
print ()

# finding average daily revenue 
av_day_rev=rev/7
print ('The average daily revenue = ${}' .format (av_day_rev))
print ()

#finding products less that $30 

less_30=[]
less_prod=[]
i=0
for price in new_price:
    if  price<30:
         less_prod.append(i)
         less_30.append(price)
    i+=1
                 

print ('Items with prices lower than $30 include: '), 
j=0
for less in less_30:
   
    print ('{} = ${}'.format(products[less_prod[j]],less_30[j]))
    j+=1
print ()
print('COME BACK NEXT WEEK FOR MORE :)')
