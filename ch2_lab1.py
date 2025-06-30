first_name= str(input("Enter your first name: "))
last_name= str(input ("Enter your last name: "))
total_marbles= int(input( "Enter the number of marbles you wish to purchase: "))
price_per_marble= 1.20
total_cost= total_marbles * price_per_marble
print ("Order prepared for " + (first_name + " " +  last_name))
print (f"{total_marbles} marbles ordered @ ${price_per_marble:.2f}") 
print (f"Total cost is $ {total_cost:.2f}")
