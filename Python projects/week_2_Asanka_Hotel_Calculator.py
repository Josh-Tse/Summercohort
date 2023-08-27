#welcome message
print ('Welcome to Asanka Hotel')
print()

# user prompt for charge
charge=input('Please type in your how much you were charged for your food')
print()

# calculations
tip = (float(charge)*18)/100
tax = (float(charge)*7)/100
total = float(charge) + tip +tax

# Final display
print("'Here's Your Bill Summary...")
print()
print('Tip = $'+ str(tip))
print()
print('Sales tax = $'+ str(tax))
print()
print('Grand total = $'+ str(total))

