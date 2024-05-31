'''if cost price & selling price of an item is input through keyboard 
write a  programm to determine wheather the seller has made 'profit' or 'incured a loss' or 'noprofit noloss'
also determine how much profit he made or loss he incured'''

cost_price=int(input("Enter the cost price in ₹:\n"))
selling_price=int(input("Enter the selling price in ₹:\n"))
if cost_price>selling_price:
    print("Incured a loss of ₹",cost_price-selling_price)
elif cost_price<selling_price:
    print("made a profit of ₹",selling_price-cost_price)
elif cost_price==selling_price:
    print("No profit, No loss")
else:
    print("cant identify")