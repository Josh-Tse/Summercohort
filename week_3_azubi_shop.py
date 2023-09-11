print ('welcome to the azubi shop portal')
print ()

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#finding price average using a for loop
for price in prices:
    av_price = av_price + price

av_price=av_price / len(price )


#updating price list

for price in prices:
    new_price.append(price-5)


#finding total revenue of products 
for price in prices:
    for item in products:
        rev = rev+(price * item)

# finding average daily revenue 
av_day_rev=rev/7
